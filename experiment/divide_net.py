# -*- coding: utf-8 -*-
"""
Created on Sat Apr 05 10:01:29 2014

@author: Administrator
"""
import math
import random
import numpy as np

def divide_net(net, ratio):
    cnt = 0
    train_edges = set()
    dim = net.shape[0]
    train = np.zeros((dim, dim), dtype = np.int)
    test = np.zeros((dim, dim), dtype = np.int)
    num = int(math.ceil(ratio * net.sum() / 2))
    while cnt < num:
        u = random.randint(0, dim - 1)
        v = random.randint(0, dim - 1)
        while v == u:
            v = random.randint(0, dim - 1)
        if v < u:
            tmp = v
            v = u
            u = tmp
        if (u, v) not in train_edges:
            train_edges.add((u, v))
            cnt += 1    
            
    for x in train_edges:
        u = x[0]
        v = x[1]
        print u, v
        train[u][v] = train[v][u] = 1
    test = net - train
    return train, test
        
        
    