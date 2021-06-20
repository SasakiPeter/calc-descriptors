from rdkit.Chem import PandasTools


def load_sdf(path):
    return PandasTools.LoadSDF(path)


def get_mols(df):
    return [mol for mol in df.ROMol]
