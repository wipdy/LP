"""
Common Neighbors

@author: DY
"""

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
            common_neig = G[i] & (G[j])
            sim[i][j] = sim[j][i] = len(common_neig)

    return sim
