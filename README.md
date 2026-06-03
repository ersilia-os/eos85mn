# FARM functional group-aware molecular representations

FARM is a molecular representation model that uses functional group-aware tokenization, bridging the gap between SMILES and natural language. FARM has been benchmarked on MoleculeNet (SOTA on most tasks) and provides atom-level and molecule-level embeddings. This model returns 768-dimensional molecule-level embeddings from the contrastive FARM BERT checkpoint.



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
- **Interpretation:** 768-dimensional molecule-level embedding from the FARM contrastive BERT model, suitable as input features for downstream property prediction. Individual dimensions are not chemically interpretable. Sequences are truncated to 512 BERT subword tokens during encoding.

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

### Resource Consumption


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
