"""
PropFlow

@author: DY
"""

import numpy as np
from collections import deque

def cal_score(G, l):
    """


    """
    
    dim = len(G)
    sim = np.zeros((dim, dim))
    for i in xrange(dim):
        BFS(i, G, l, sim)

    return sim


def BFS(s, G, l, sim):
    """

    """
    
    que = deuqe([s])
    depth = {s:0}
    node_input = {s:1.}
    while que:
        u = que.popleft()
        if depth[u] > l:
            break

        sum_w = 0.
        for v in G[u]:
            if (depth.has_key(v) == False) or (depth[v] > depth[u]):
                sum_w += G[u][v]

        for v in G[u]:
            if (depth.has_key(v) == False) or (depth[v] > depth[u]):
                flow = node_input[u] * (G[u][v] / sum_w)
                node_input[v] = node_input.get(v, 0.) + flow

                if depth.has_key(v) == False:
                    depth[v] = depth[u] + 1
                    que.append(v)

    for v in node_input:
        sim[s][v] = node_input[v]

        
'''
que = deque([3, 2, 1])
print len(que) 
for x in que:
    print x,
print ''
que.popleft()
for x in que:
    print x,
print ''

while que:
    print que.popleft(),
dict = {'a':1, 'b':2, 'c':3}
if 'a' in dict:
    print dict['a']
dict['d'] = 0.5
print dict['d']
    
l = 5
#sim = np.array()
neig = []
def predict_line(train):
    dim = train.shape[0]
    sim = np.array((dim, dim), dtype = float)
    sim.resize(dim, dim)
    for i in range(dim):
        neig.append(set())
        for j in range(dim):
            if train[i][j]:
                neig[i].add(j)
    
    for i in range(dim):
        cal_sim(train, sim, i, l)
        
    return sim

def cal_sim(G, sim, s, l):
    que = deque([s])
    depth = {s:0}
    node_input = {s:1.}
    while que:
        u = que.popleft()
        if depth[u] > l:
            break;
        sum_w = 0.
        for v in neig[u]:
            if (v not in depth) or (depth[v] > depth[u]):
                sum_w += G[u][v]
        
        for v in neig[u]:
            if (v not in depth) or (depth[v] > depth[u]):
                flow = node_input[u] * (G[u][v] / sum_w)
                node_input[v] = node_input.get(v, 0.) + flow
                if v not in depth:
                    depth[v] = depth[u] + 1
                    que.append(v)
    
    for v in node_input:
        sim[s][v] = node_input[v]
'''
