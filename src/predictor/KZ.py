"""
Katz

@author: DY
"""

import numpy as np

def cal_score(G, beta):
    """
    Calculate the similarity score according to Katz index.

    Parameters
    ----------
    G: list
        A adjacency list. The nodes are indexed from 0. 
        The ith element of G is a set containing its neighbors.
    beta: float
        The damping factor.

    Returns
    -------
    sim: ndarray
        A n by n matrix where n is the number of all
        nodes. The element sim[i][j] represents the 
        similarity between the ith node and the jth node.
    """

    dim = len(G)
    mat = conv2mat(G)
    sim = np.linalg.inv(np.eye(dim) - beta * mat) - np.eye(dim)

    return sim


def conv2mat(G):
    """
    Convert graph from adjacency list to adjacency matrix.

    Parameters
    ----------
    G: list
        A adjacency list. The nodes are indexed from 0. 
        The ith element of G is a set containing its neighbors.

    Returns
    -------
    mat: ndarray
        A n by n matrix where n is the number of all
        nodes. The element mat[i][j] equals 1 if there
        is an edge between the ith node and the jth node,
        otherwise mat[i][j] equals 0.
    """

    dim = len(G)
    mat = np.zeros((dim, dim), dtype = np.int)
    for i in G:
        for j in G[i]:
            mat[i][j] = 1

    return mat


def predict_link(train, beta):
    dim = train.shape[0]
    sim = np.linalg.inv(np.eye(dim, dtype = np.float) - beta * train) - np.eye(dim, dtype = np.float)
    return sim
