# FARM functional group-aware molecular representations

FARM builds a 768-dimensional embedding around functional groups, tokenising SMILES so that recognised chemical moieties become units the language model sees directly rather than fragments it must infer. Nguyen and colleagues designed this to close the gap between how chemists reason about molecules and how sequence models read them, aligning the learned representation with structural intuition. Sequences are truncated during encoding, so very large molecules are represented only in part.

This model was incorporated on 2025-08-27.Last packaged on 2026-06-03.

## Information
### Identifiers
- **Ersilia Identifier:** `eos85mn`
- **Slug:** `farm-representation`

### Domain
- **Task:** `Representation`
- **Subtask:** `Featurization`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `Embedding`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `768`
- **Output Consistency:** `Fixed`
- **Interpretation:** 768 features encoding molecular structure from a functional-group-aware language model.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| feat_000 | float |  | FARM molecule-level embedding dimension 000 |
| feat_001 | float |  | FARM molecule-level embedding dimension 001 |
| feat_002 | float |  | FARM molecule-level embedding dimension 002 |
| feat_003 | float |  | FARM molecule-level embedding dimension 003 |
| feat_004 | float |  | FARM molecule-level embedding dimension 004 |
| feat_005 | float |  | FARM molecule-level embedding dimension 005 |
| feat_006 | float |  | FARM molecule-level embedding dimension 006 |
| feat_007 | float |  | FARM molecule-level embedding dimension 007 |
| feat_008 | float |  | FARM molecule-level embedding dimension 008 |
| feat_009 | float |  | FARM molecule-level embedding dimension 009 |

_10 of 768 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos85mn](https://hub.docker.com/r/ersiliaos/eos85mn)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos85mn.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos85mn.zip)

### Resource Consumption
- **Model Size (Mb):** `394`
- **Environment Size (Mb):** `1370`
- **Image Size (Mb):** `2146.62`

**Computational Performance (seconds):**
- 10 inputs: `33.68`
- 100 inputs: `28.64`
- 10000 inputs: `500.77`

### References
- **Source Code**: [https://github.com/thaonguyen217/farm_molecular_representation](https://github.com/thaonguyen217/farm_molecular_representation)
- **Publication**: [https://doi.org/10.48550/arXiv.2410.02082](https://doi.org/10.48550/arXiv.2410.02082)
- **Publication Type:** `Preprint`
- **Publication Year:** `2024`
- **Ersilia Contributor:** [AnshikaVashistha](https://github.com/AnshikaVashistha)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [MIT](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos85mn
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos85mn
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
