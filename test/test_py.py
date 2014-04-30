import numpy as np

path = 'C:/Users/Administrator/Desktop/'
fname = 'input.txt' #USAir.txt'
f = open(path + fname)
max = -1
edges = set()

for line in f:
    x = str(line).split()
    edges.add((int(x[0]), int(x[1])))
    if int(x[0]) > max:
        max = int(x[0])
    if int(x[1]) > max:
        max = int(x[1])

for x in edges:
    print x
mat = np.zeros((max, max), dtype = np.int)
for x in edges:
    u = x[0] - 1
    v = x[1] - 1
    mat[u][v] = mat[v][u] = 1
print shape(mat)[0], shape(mat)[1]

print mat.shape[0], mat.shape[1]

print mat.sum()

print ceil(13.1)
'''
for i in range(shape(mat)[0]):
    for j in range(shape(mat)[1]):
        print mat[i][j],
    print ''
'''
'''
mat = np.zeros((333, 333), dtype = np.int)
for line in f:
    x = str(line).split()
    mat[int(x[0])][int(x[1])] = mat[int(x[1])][int(x[0])] = 1
    
for i in range(333):
    if mat[i][i] != 0:
        print i
        
ls = [0 for i in range(10)]
print len(ls)

for i in range(10):
    print i, ls[i]

#for x in ls:
#    print x

for line in f:
    x = str(line).split()
#    print int(x[0]), int(x[1])

    if int(x[0]) > max:
        max = int(x[0])
    if int(x[1]) > max:
        max = int(x[1])
#ls = [0 for i in range(max + 1)]
print max
print 'ok?'

ls = [0 for i in range(333)]
for line in f:
    x = str(line).split()
    ls[int(x[0])] += 1
    ls[int(x[1])] += 1

for i in range(333):
    if ls[i] == 0:
        print i
'''