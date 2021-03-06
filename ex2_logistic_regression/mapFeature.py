#!/usr/bin/env python
# -*- coding: utf-8 -*-


def mapFeature(X1, X2):
    degree = 6
    out = []
    from math import pow
    for r in range(len(X1)):
        row = []
        for i in range(degree + 1):
            for j in range(i + 1):
                xx = pow(X1[r], i - j) * pow(X2[r], j)
                row.append(xx)
        out.append(row)
    import numpy as np
    return np.asarray(out)
