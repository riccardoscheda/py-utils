#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from re import A
from ml.data_utils import df_to_numpy

import numpy as np
import pandas as pd

import pytest

def test_df_to_numpy(iris, multiidx_df):

    # Test with a single index array
    assert isinstance(iris, pd.DataFrame)

    iris_array = df_to_numpy(iris)
    assert isinstance(iris_array, np.ndarray)
    assert iris_array.shape == iris.shape

    # Test with a multindexed array
    assert isinstance(multiidx_df, pd.DataFrame)

    arr = df_to_numpy(multiidx_df)
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (3, 2, 2)


if __name__ == '__main__':
    test_df_to_numpy()