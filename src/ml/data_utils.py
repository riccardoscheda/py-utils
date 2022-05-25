#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

def df_to_numpy(df: pd.DataFrame) -> np.array:
    """This function accepts a dataframe with a MultiIndex and return a numpy ndarray

    Parameters
    ----------
    df : pd.DataFrame
        dataframe with MultiIndex

    Returns
    -------
    np.array
        ndarray
    """

    try:
        shape = [len(level) for level in df.index.levels]

    except AttributeError:
        shape = [len(df.index)]

    ncol = df.shape[-1]
    if ncol > 1:
        shape.append(ncol)

    return df.to_numpy().reshape(shape)


if __name__ == '__main__':
    pass