import sys
from collections import deque


def printMatrix(matrix, spacingfactor=3):
    for i in range(len(matrix)):
        print('')
        for j in range(len(matrix[i])):
            if matrix[i][j] == None:
                sp = spacingfactor-4
                e1 = ' '*sp
                print(matrix[i][j], end=e1)
            else:
                l = len(str(matrix[i][j]))
                e = ' '*spacingfactor
                end = e[:-l]
                print(matrix[i][j], end=end)

indexes = {}
index = 1

numofchildren, numoftoys, numofcat = input().split()
numofchildren = int(numofchildren)
numoftoys = int(numoftoys)
numofcat = int(numofcat)
residualmatrix = []
indexes['s'] = index
index = index + 1
matrixSize = numofchildren + numoftoys + numofcat + 3


matrix = [[0 for i in range(matrixSize)] for j in range(matrixSize)]

parseindex = 2
matrix[0][1] = 's'
matrix[1][0] = 's'


for i in range(numofchildren):
    num = 'b' + str(i+1)
    matrix[0][parseindex] = num
    matrix[parseindex][0] = num
    matrix[1][parseindex] = 1
    indexes[num] = index
    index = index + 1
    parseindex += 1


for i in range(numoftoys):
    num = 't' + str(i+1)
    matrix[0][parseindex] = num
    matrix[parseindex][0] = num
    indexes[num] = index
    index = index + 1
    parseindex += 1


for i in range(numofcat):
    num = 'c' + str(i+1)
    matrix[0][parseindex] = num
    matrix[parseindex][0] = num
    indexes[num] = index
    index = index + 1
    parseindex += 1

matrix[0][parseindex] = 't'
matrix[parseindex][0] = 't'
indexes['t'] = index
index = index + 1

parseindex = 2

sinkidx = indexes['t']

for i in range(numofchildren):
    k = input().split()
    r = int(k[0])
    for j in range(r):
        toynum = k[j+1]
        toyidx = indexes['t'+toynum]
        matrix[i+2][toyidx] = 1

for i in range(numoftoys):
    toyidx = indexes['t' + str(i+1)]
    matrix[toyidx][sinkidx] = 1

for i in range(numofcat):
    k = input().split()
    catindex = indexes['c' + str(i+1)]
    r = int(k[0])
    c = int(k.pop())
    for j in range(r):
        toynum = k[j+1]
        toyidx = indexes['t'+toynum]
        matrix[toyidx][catindex] = 1
        matrix[toyidx][sinkidx] = 0
    matrix[catindex][sinkidx] = c


bottleneck = 1
def dfs(source, sink):
    pathlist = []
    stack = deque([])
    visited = set()
    parentMap = {}
    stack.append(source)
    t_reached = False

    while len(stack) > 0:
        currentnode = stack.pop()
        currentnodeindex = indexes[currentnode]

        if currentnode not in visited:
            visited.add(currentnode)

        pathlist.append(currentnode)

        if currentnode == sink:
            t_reached = True
            break

        for i in range(1, len(matrix[currentnodeindex])):
            if matrix[0][i] not in visited and matrix[currentnodeindex][i] > 0:
                stack.append(matrix[0][i])
                parentMap[matrix[0][i]] = currentnode

    return pathlist, t_reached, parentMap

maxflow = 0
treached = True


while True:
    path = []
    pathlist, treached, parentMap = dfs('s', 't')
    if not treached:
        break
    maxflow += bottleneck
    v = 't'
    while v != 's':
        path.append(v)
        u = parentMap[v]
        v_idx = indexes[v]
        u_idx = indexes[u]
        matrix[u_idx][v_idx] = matrix[u_idx][v_idx] - bottleneck
        matrix[v_idx][u_idx] = matrix[v_idx][u_idx] + bottleneck
        v = parentMap[v]

    path.append(v)

print(maxflow)