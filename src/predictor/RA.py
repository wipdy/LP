"""
Resource Allocation

@author: DY
"""

import numpy as np

def cal_score(G):
    """
    Calculate the similarity score according to resource
    allocation index.

    Parameters
    ----------
    G: list
        A adjacency list. The nodes are indexed from 0.
        The ith element of G is a set containing its neighbors.

    Returns
    -------
    sim: ndarray
        A n by n matrix where n is the number of all
        nodes. The element sim[i][j] represents the 
        similarity between the ith node and the jth node.
    """

    dim = len(G)
    sim = np.zeros((dim, dim))
    for i in xrange(dim):
        for j in xrange(i + 1, dim):
            common_neig = G[i] & G[j]
            for z in common_neig:
                sim[i][j] += (1. / len(G[z]))

            sim[j][i] = sim[i][j]

    return sim


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
                sim[i][j] += (1.0 / len(neig[z]))
            sim[j][i] = sim[i][j]
    return sim
    
