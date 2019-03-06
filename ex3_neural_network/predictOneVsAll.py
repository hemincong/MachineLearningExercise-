#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


def predictOneVsAll(all_theta, X):
    m, n = X.shape

    num_labels, _ = all_theta.shape
    p = np.zeros((m, 1))
    X = np.insert(X, 0, 1, axis=1)

    from utils.sigmoid import sigmoid

    max_value = sigmoid(np.dot(X, all_theta.T))
    p = max_value.argmax(axis=1)
    return p
