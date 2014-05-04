"""
unit test

@author: DY
"""

import numpy as np
import sys

sys.path.append('./predictor/')

import JC

def predict_link(train):
    dim = train.shape[0]
    neig = [set() for i in range(dim)]  
    for i in range(dim):
        for j in range(dim):
            if train[i][j]:
                neig[i].add(j)

                
    sim = np.zeros((dim, dim), dtype = np.float)
    for i in range(dim):
        for j in range(dim):
            if len(neig[i] | neig[j]) > 0:
                sim[i][j] = float(len(neig[i] & neig[j])) / (len(neig[i] | neig[j]))
    return sim
    


def test():
    kase = 20
    for __ in xrange(kase):
        G, train = gen_graph()        
        sim1 = JC.cal_score(G)
        sim2 = predict_link(train)
        print 'test case: ', __  + 1
        if valid(sim1, sim2):
            print 'OK'
        else:
            print 'error'
            print train
            print 'sim1'
            print sim1
            print 'sim2'
            print sim2
            break


def gen_graph():
    import random
    dim = random.randint(3, 15)
    G = [set() for __ in xrange(dim)]
    train = np.zeros((dim, dim), dtype = int)
    num_ee = random.randint(1, dim * (dim - 1) / 2)
    for __ in xrange(num_ee):
        u = random.randint(0, dim - 1)
        v = random.randint(0, dim - 1)
        if u != v:
            train[u][v] = train[v][u] = 1
            G[u].add(v)
            G[v].add(u)

    return G, train


def valid(sim1, sim2):
    EPS = 1E-6
    #if sim1.shape[0] == sim2.shape[0] and \
    #        sim1.shape[1] == sim2.shape[1]:
    if sim1.shape == sim2.shape:
        dim = sim1.shape[0]
        for i in xrange(dim):
            for j in xrange(i + 1, dim):
                if abs(sim1[i][j] - sim2[i][j]) > EPS:
                    return False
        return True
    
    return False

if __name__ == '__main__':
    test()
