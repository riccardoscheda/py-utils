#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import io
import pytest

import pandas as pd
from sklearn.datasets import load_iris


# scope='session' means that the same value of "iris" will be shared between test (1 download)
@pytest.fixture(scope='session')
def iris():

    data = load_iris()

    yield pd.DataFrame(data['data'], columns=data['feature_names'])

@pytest.fixture(scope='session')
def multiidx_df():

    data = io.StringIO('''Fruit,Color,Count,Price
                        Apple,Red,3,$1.29
                        Apple,Green,9,$0.99
                        Pear,Red,25,$2.59
                        Pear,Green,26,$2.79
                        Lime,Green,99,$0.39
                        Lime,Red,,
                        ''')

    df_unindexed = pd.read_csv(data)
    yield df_unindexed.set_index(['Fruit', 'Color'])


# This fixture capture the std output
@pytest.fixture
def capture_stdout(monkeypatch):

    buffer = {'stdout': '', 'write_calls': 0}

    def fake_write(s):
        buffer['stdout'] += s
        buffer['write_calls'] += 1

    monkeypatch.setattr(sys.stdout, 'write', fake_write)
    return buffer
