# -*- coding: utf-8 -*-

import math
import numpy as np

K = 50
def predict_link(train, theta):
    dim = train.shape[0]
    neig = [set() for i in range(dim)]
    for i in range(dim):
        for j in range(dim):
            if train[j][i]:
                neig[i].add(j)
                
    sim = np.eye(dim, dtype = np.float)
    for i in range(K):
        tmp = np.eye(dim, dtype = np.float)
        for i in range(dim):
            for j in range(i + 1, dim):
                for x in neig[i]:
                    for y in neig[j]:
                        tmp[i][j] += sim[x][y]
                tmp[i][j] = tmp[i][j] * theta / (len(neig[i]) * len(neig[j]))
                tmp[j][i] = tmp[i][j]
        sim = tmp
    return sim