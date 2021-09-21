#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_validate


class NestedCV(object):
    '''
    Object that performs a nested cross validation with any scikit learn compatible model

    Parameters
    ----------

    model: sklearn compatible model
        an instance of the model that need to be tested

    params: dictionary
        dictionary of the parameters passed to a GridSearchCV object

    scoring: list
        list of scoring functions used during model evaluation (passed to GridSearchCV)

    refit: str
        name of the refit function. Must be contained inside the list "scoring". passed to GridSearchCV

    inner_splits: int
        number of inner splits for KFold

    outer_splits: int
        number of outer splits for KFold

    n_jobs: int
        number of workers. Passed to GridSearchCV and cross_validate function

    rnd_state: int
        random seed of the system

    '''

    def __init__(self,
                 model,
                 params: dict,
                 scoring: list = ['neg_mean_squared_error'],
                 refit: str = 'neg_mean_squared_error',
                 inner_splits: int = 5,
                 outer_splits: int = 3,
                 n_jobs: int = 1,
                 rnd_state: int = None):

        self.model = model
        self.scoring = scoring
        self.n_jobs = n_jobs
        self.outer_splits = outer_splits
        self.rnd_state = rnd_state

        self.inner_cv = KFold(n_splits=inner_splits, shuffle=True, random_state=self.rnd_state)
        self.outer_cv = KFold(n_splits=outer_splits, shuffle=True, random_state=self.rnd_state)

        self.gcv = GridSearchCV(model, params, cv=self.inner_cv, refit=refit, scoring=self.scoring, n_jobs=self.n_jobs)

    def get_scoring(self) -> list:
        return self.scoring

    @property
    def model_name(self) -> str:
        return str(model).split('(')[0]

    def get_scores(self) -> pd.DataFrame:
        return self.scores

    def get_gcv(self) -> GridSearchCV:
        return self.gcv

    def fit(self, X, y) -> pd.DataFrame:

        scores = cross_validate(self.gcv, X=X, y=y, scoring=self.scoring, cv=self.outer_cv, n_jobs=self.n_jobs)

        # Tranform scores in nice pandas df
        scores['model'] = [self.model_name] * self.outer_splits
        scores['cv_split'] = np.arange(1, self.outer_splits + 1)

        if self.rnd_state:
            scores['rnd_state'] = [self.rnd_state] * self.outer_splits

        scores['n_samples_tot'] = [len(X)] * self.outer_splits
        scores['n_samples_split'] = [len(X) // self.outer_splits] * self.outer_splits

        self.scores = pd.DataFrame(scores)

        return self.scores


if __name__ == '__main__':

    from sklearn.linear_model import Ridge
    from sklearn.datasets import load_boston

    model = Ridge()
    params = {'alpha': [0.001, 0.01, 0.1, 0.5, 1]}

    obj = NestedCV(model=model,
                   params=params,
                   scoring=['neg_mean_squared_error', 'neg_mean_absolute_error'],
                   refit='neg_mean_squared_error',
                   inner_splits=5,
                   outer_splits=3,
                   n_jobs=2,
                   rnd_state=1)

    data = load_boston()

    X = data['data']
    y = data['target']

    score = obj.fit(X, y)
    score
