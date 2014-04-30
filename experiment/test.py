# -*- coding: utf-8 -*-

import math
import random
import numpy as np

import preprocess as prep
import SimRank

dim = 50
num_edges = 800 
path = 'C:\\Users\\Administrator\\Desktop\\test\\'
in_fn = 'in.txt'
out_fn = 'my.txt'
def gen_data():
    cnt = 0
    f = open(path + in_fn, 'w')
    while cnt < num_edges:
        u = random.randint(1, dim)
        v = random.randint(1, dim)
        if u != v:
            f.write(str(u) + ' ' + str(v) + '\n')
            cnt += 1
    f.close()

def output_mat(mat, fn):
    f = open(fn, 'w')
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            f.write(str(mat[i][j]) + ' ')
        f.write('\n')
    f.close()

#square matrix    
def read_mat(fn):
    f = open(fn, 'r')
    dim = len(str(f.readline()).split())
    f.close()
    
    
    f = open(fn, 'r')
    mat = np.zeros((dim, dim), dtype = np.float)
    i = j = 0
    for line in f:
#        print line        
        nums = str(line).split()
        j = 0
        for x in nums:
 #           print float(x),
            mat[i][j] = float(x)
            j += 1
        i += 1
#        print ''
    f.close()
    return mat

            
EPS = 1e-3
def cmp_mat(mat1, mat2):
    if mat1.shape[0] != mat2.shape[0] or mat1.shape[1] != mat2.shape[1]:
        return False
    for i in range(mat1.shape[0]):
        for j in range(i + 1, mat2.shape[1]):
            if math.fabs(mat1[i][j] - mat2[i][j]) > EPS:
                print i, j
                return False
    return True
    
def test():
    edges = prep.read_edges(path + in_fn)
    net = prep.build_net(edges)
    
    my = SimRank.predict_link(net, 0.8)
    output_mat(my, path + 'my.txt')
    oth = read_mat(path + 'oth.txt')        

    print cmp_mat(my, oth)

#gen_data()    
test()
