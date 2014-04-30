# -*- coding: utf-8 -*-
"""
Created on Sat Apr 05 14:55:21 2014

@author: Administrator
"""

import numpy as np

def predict_link(train):
    dim = train.shape[0]
    neig = [set() for i in range(dim)]  
    for i in range(dim):
        for j in range(dim):
            if train[i][j]:
                neig[i].add(j)
                
    sim = np.zeros((dim, dim), dtype = np.float)
    for i in range(dim):
        for j in range(dim):
            sim[i][j] = float(len(neig[i] & neig[j])) / (len(neig[i] | neig[j]))
    return sim
    
    
'''    
n1 = set()
n2 = set()    
for i in range(5):
    n1.add(i)
for i in range(3, 10):
    n2.add(i)
for x in n1 & n2:
    print x
'''