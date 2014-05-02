import numpy as np

import CN

def predict_link(train):
    return train.dot(train)


def test():
    kase = 20
    for __ in xrange(kase):
        G, train = gen_graph()        
        sim1 = CN.cal_score(G)
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
    dim = random.randint(3, 10)
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
            for j in xrange(dim):
                if abs(sim1[i][j] - sim2[i][j]) > EPS:
                    return False
        return True
    
    return False

if __name__ == '__main__':
    test()
