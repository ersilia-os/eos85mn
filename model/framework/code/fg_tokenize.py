# FG-enhanced SMILES conversion from FARM (MIT License).
# Vendored from farm_molecular_representation src/helpers.py (main branch).

from rdkit.Chem import MolFromSmiles

from farm_fg_helpers import get_new_smiles_rep


def smiles_to_fg_enhanced(smiles: str) -> str:
    """Convert a SMILES string to FG-enhanced FARM tokens."""
    mol = MolFromSmiles(smiles)
    if mol is None:
        raise ValueError(f"Invalid SMILES: {smiles}")

    return get_new_smiles_rep(mol).strip()
