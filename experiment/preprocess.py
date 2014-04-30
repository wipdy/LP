# -*- coding: utf-8 -*-
"""
Created on Sat Apr 05 15:40:52 2014

@author: Administrator
"""

import math
import random
import numpy as np     

def read_edges(fn):
    f = open(fn)
    edges = set()
    for line in f:
        x = str(line).split()
        u = int(x[0])
        v = int(x[1])
        edges.add((u, v))
    f.close()
    return edges

#indexed from 0
def build_net(edges):
    dim = 0
    for x in edges:
        if x[0] > dim:
            dim = x[0]
        if x[1] > dim:
            dim = x[1]
    mat = np.zeros((dim, dim), dtype = np.int)
    for x in edges:
        u = x[0] - 1
        v = x[1] - 1
        mat[u][v] = mat[v][u] = 1
    return mat


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
        if net[u][v] and (u, v) not in train_edges:
            train_edges.add((u, v))
            cnt += 1    
            
    for x in train_edges:
        u = x[0]
        v = x[1]
#        print u, v
        train[u][v] = train[v][u] = 1
    test = net - train
    return train, test
        
        
    