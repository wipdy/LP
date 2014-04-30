# -*- coding: utf-8 -*-
"""
Created on Sat Apr 05 14:57:05 2014

@author: Administrator
"""

import math
import numpy as np

def predict_link(train):
    dim = train.shape[0]
    neig = [set() for i in range(dim)]
    for i in range(dim):
        for j in range(i + 1, dim):
            if train[i][j]:
                neig[i].add(j)
                neig[j].add(i)
            
    sim = np.zeros((dim, dim), dtype = np.float)
    for i in range(dim):
        for j in range(i + 1, dim):
            for z in neig[i] & neig[j]:
                sim[i][j] += (1.0 / math.log(len(neig[z])))
            sim[j][i] = sim[i][j]
    return sim
    
#print math.log(8, 2)