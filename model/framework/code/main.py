import os
import sys

import numpy as np
import torch
from transformers import BertForMaskedLM, PreTrainedTokenizerFast

from ersilia_pack_utils.core import read_smiles, write_out

from fg_tokenize import smiles_to_fg_enhanced

# Weights are fetched at build time and bundled under model/checkpoints/
# (see access.json); they are not downloaded from HuggingFace at inference time.
ROOT = os.path.dirname(os.path.abspath(__file__))
CHECKPOINTS_DIR = os.path.abspath(os.path.join(ROOT, "..", "..", "checkpoints"))

EMBED_DIM = 768
MAX_LEN = 512


def load_model():
    tokenizer = PreTrainedTokenizerFast.from_pretrained(CHECKPOINTS_DIR)
    model = BertForMaskedLM.from_pretrained(CHECKPOINTS_DIR)
    model.to("cpu")
    model.eval()
    return tokenizer, model


def embed_one(tokenizer, model, smiles: str) -> np.ndarray:
    """Molecule-level embedding; mean pool over attention-masked tokens."""
    fg_text = smiles_to_fg_enhanced(smiles)
    inputs = tokenizer(
        fg_text,
        return_tensors="pt",
        truncation=True,
        max_length=MAX_LEN,
    )
    with torch.no_grad():
        outputs = model(**inputs, output_hidden_states=True)
    last_hidden = outputs.hidden_states[-1][0]
    attention_mask = inputs["attention_mask"][0]
    masked = last_hidden * attention_mask.unsqueeze(-1)
    summed = masked.sum(dim=0)
    count = attention_mask.sum().clamp(min=1)
    pooled = summed / count
    return pooled.cpu().numpy().astype(np.float32)


def main(input_file: str, output_file: str) -> None:
    header, smiles_list = read_smiles(input_file)
    tokenizer, model = load_model()

    results = []
    for smi in smiles_list:
        try:
            emb = embed_one(tokenizer, model, smi)
        except (ValueError, RuntimeError):
            emb = np.full((EMBED_DIM,), np.nan, dtype=np.float32)
        results.append(emb)

    out_header = [f"feat_{i:03d}" for i in range(EMBED_DIM)]
    write_out(
        np.array(results, dtype=np.float32),
        out_header,
        output_file,
        np.float32,
    )


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
