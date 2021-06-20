from .load import get_mols
import numpy as np
import pandas as pd
from tqdm import tqdm
from mordred import Calculator, descriptors
import mordred
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from logger import setup_logger  # NOQA


__all__ = ('join_descs_to_df',)


def calc_descs(mols):
    return Calculator(descriptors, ignore_3D=False).pandas(mols)


def convert_error_to_nan(descs):
    for i, col_val in tqdm(enumerate(descs.values.tolist())):
        for j, val in enumerate(col_val):
            if isinstance(val, mordred.error.Missing):
                descs.iloc[i, j] = np.nan
            elif isinstance(val, bool):
                descs.iloc[i, j] = val + 0
    return descs


def join_descs_to_df(sdf, label):
    logger = setup_logger(__name__)
    descs = convert_error_to_nan(calc_descs(get_mols(sdf)))
    logger.info(f'descs shape: {descs.shape}')
    logger.info(f'num of null: {descs.isnull().sum().sum()}')
    return pd.concat([label, descs], axis=1)
