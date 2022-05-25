#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#%%

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

#%%

if __name__ == '__main__':

    # Usage example
    import pandas as pd
    import io

    data = io.StringIO('''Fruit,Color,Count,Price
                    Apple,Red,3,$1.29
                    Apple,Green,9,$0.99
                    Pear,Red,25,$2.59
                    Pear,Green,26,$2.79
                    Lime,Green,99,$0.39
                    Lime,Red,,
                    ''')

    df_unindexed = pd.read_csv(data)
    df = df_unindexed.set_index(['Fruit', 'Color'])
    arr = df_to_numpy(df)
# %%



