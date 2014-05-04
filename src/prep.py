# -*- coding: utf-8 -*-
"""
preprocess

@author: DY 
"""

import numpy as np     

def read_data(fn):
    f = open(fn)
    rds = []
    for line in f:
        rds.append(line.strip().split())

    f.close()

    return rds

def build_graph(rds):
    """
    undirected unweighted
    """

    vertex_cnt = 0
    vertex_index = {}
    for line in rds:
        if vertex_index.has_key(line[0]) == False:
            vertex_index[line[0]] = vertex_cnt
            vertex += 1

        if vertex_index.has_key(line[1]) == False:
            vertex_index[line[1]] = vertex_cnt
            vertex += 1
        
    
    G = []
    for i in xrange(vertex_cnt):
        G.append(set())

    for line in rds:
        u = vertex_index[line[0]]
        v = vertex_index[line[1]]
        G[u].add(v)
        G[v].add(u)

    return G

"""
def build_graph(rds, opt = 0):
    if opt == 0:
    elif opt == 1:
        for i in xrange(vertex_cnt):
            G.append({})
    
    else:
        for i in xrange(vertex_cnt):
            G.append({})
"""


def divide_data(rds, ratio):
    train = []
    test = []
    selected = [0 for __ in xrange(len(rds))]

    cnt = 0
    while cnt < int(ratio * len(rds)):
        pos = np.random.randint(len(rds))
        if selected[pos] == 0:
            selected[pos] = 1
            cnt += 1

    for i in xrange(len(rds)):
        if selected[i] == 1:
            train.append(rds[i])
        else:
            test.append(rds[i])

    return train, test

    
