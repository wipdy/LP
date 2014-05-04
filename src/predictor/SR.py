"""
SimRank

@author: DY
"""

import math
import numpy as np

def cal_score(G, theta, K):
    """
    Calculate the similarity score according to SimRank.

    Parameters
    ----------
    G: list 
        A adjacency list. The nodes are indexed from 0.
        The ith element of G is a set containing its neighbors.
    theta: float
        The decay factor.
    K: int
        Iteration time.

    Returns
    -------
    sim: ndarray
        A n by n matrix where n is the number of all
        nodes. The element sim[i][j] represents the
        similarity between the ith node and the jth node.
    """

    dim = len(G)
    sim = np.eye(dim)
    for __ in xrange(K):
        mat = np.eye(dim)
        for i in xrange(dim):
            for j in xrange(i + 1, dim):
                for x in G[i]:
                    for y in G[j]:
                        mat[i][j] += sim[x][y]

                mat[i][j] = mat[i][j] * theta / (len(G[i]) * len(G[j]))
                mat[j][i] = mat[i][j]

        sim = mat

    return sim

"""
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


def test():
    G = [set() for __ in xrange(5)]
    mat = np.zeros((5, 5))
    for __ in xrange(6):
        u, v, x = map(int, raw_input().split())
        G[u].add(v)
        G[v].add(u)
        mat[u][v] = mat[v][u] = 1

    for i in xrange(5):
        print mat[i][0], 
        for j in xrange(1, 5):
            print ',', mat[i][j], 

    ret = cal_score(G, 0.8, 10000)
    dim = ret.shape[0]
    for i in xrange(dim):
        for j in xrange(dim):
            print ret[i][j]

if __name__ == '__main__':
    test()
"""
