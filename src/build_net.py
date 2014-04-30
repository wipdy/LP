# -*- coding: utf-8 -*-
"""
Created on Sat Apr 05 09:55:11 2014

@author: Administrator
"""

import numpy as np

#indexed from 0

def build_net(edges, dim):
    mat = np.zeros((dim, dim))
    for x in edges:
        u = x[0] - 1
        v = x[1] - 1
        mat[u][v] = mat[v][u] = 1
    return mat