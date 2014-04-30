# -*- coding: utf-8 -*-
"""
Created on Sat Apr 05 15:11:46 2014

@author: Administrator
"""

import random

def cal_AUC(train, test, sim, n):
    dim = train.shape[0]
    non = train - test
    dict_test = {}
    dict_non = {}
    for i in range(dim):
        for j in range(i + 1, dim):
            if test[i][j]:
                dict_test[len(dict_test)] = sim[i][j]
            if non[i][j]:
                dict_non[len[dict_non]] = sim[i][j]
        
    n1 = 0
    n2 = 0
    while n:
        n -= 1
        x = random.randint(0, len(dict_test))
        y = random.randint(0, len(dict_non))
        if dict_test[x] > dict_non[y]:
            n1 += 1
        else:
            n2 += 1
    AUC = (n1 + 0.5 * n2) / n
    return AUC
    

def cal_precision(train, test, sim, L):
    dim = train.shape[0]
    non = train - test
    ls = {}
    for i in range(dim):
        for j in range(i + 1, dim):
            if test[i][j] or non[i][j]:
                ls[(i, j)] = ls.get((i, j), 0.) + sim[i][j]
    ls = sorted(ls.iteritems(), key = lambda d:d[1], reverse = True)
    cnt = 0
    for i in range(L):
        u = ls[i][0][0]
        v = ls[i][0][1]
        if test[u][v]:
            cnt += 1
    res = float(cnt) / L
    return res
    
