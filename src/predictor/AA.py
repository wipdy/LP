"""
Adamic-Adar

@author: DY
"""

import math
import numpy as np

def cal_score(G):
    """
    Parameters
    ----------
    G: list
        A undirected graph of the network. The nodes are
        indexed from 0. The ith element of G is a set
        containing its neighors.

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
                if len(G[z]) != 1:
                    sim[i][j] += (1. / math.log(len(G[z])))
            sim[j][i] = sim[i][j]

    return sim

