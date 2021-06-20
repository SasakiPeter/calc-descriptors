import pandas as pd
from .calc_descs import join_descs_to_df
from .load import load_sdf
from .parser import *  # NOQA


def get_df_with_descs(sdf_path, label_path):
    return join_descs_to_df(load_sdf(sdf_path), pd.read_csv(label_path))
