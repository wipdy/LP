# -*- coding: utf-8 -*-
"""
Created on Sat Apr 05 14:57:23 2014

@author: Administrator
"""

import numpy as np

def predict_link(train):
    dim = train.shape[0]
    neig = [set() for i in range(dim)]
    for i in range(dim):
        for j in range(i + 1, dim):
            if train[i][j]:
                neig[i].add(j)
                neig[j].add(i)
            
    sim = np.zeros((dim, dim), dtype = np.int)
    for i in range(dim):
        for j in range(i + 1, dim):
            sim[i][j] = sim[j][i] = len(neig[i]) * len(neig[j])
    return sim
    