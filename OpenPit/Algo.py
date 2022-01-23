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
    print()


indexes = {}
index = 1

numofblocks = int(input())

residualmatrix = []
indexes['s'] = index
index = index + 1
matrixSize = numofblocks + 3

matrix = [[0 for i in range(matrixSize)] for j in range(matrixSize)]


#
parseindex = 2
matrix[0][1] = 's'
matrix[1][0] = 's'



for i in range(numofblocks):
    num = 'b' + str(i+1)
    matrix[0][parseindex] = num
    matrix[parseindex][0] = num
    #matrix[1][parseindex] = 1
    indexes[num] = index
    index = index + 1
    parseindex += 1

t_index = numofblocks+2

matrix[t_index][0] = "t"
matrix[0][t_index] = "t"
sum_pos = 0

for i in range(numofblocks):
    b = list(map(int, input().split()))
    profit = b[0] - b[1]
    obsnum = b[2]
    b_obs = b[-obsnum:]
    if profit > 0:
        matrix[1][i+2] = profit
        sum_pos = sum_pos + profit
    else:
        matrix[i+2][t_index] = abs(profit)

    if obsnum > 0:
        for obs in b_obs:
            matrix[obs+1][i+2] = float('inf')

#print("sumpos", sum_pos)
indexes['t'] = index

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



bottleneck = float('inf')

maxflow = 0
treached = True

while True:
    path = []
    pathlist, treached, parentMap = dfs('s', 't')
    if not treached:
        break
    for i in range(1, len(pathlist)):
        node = indexes[pathlist[i]]
        parent = indexes[parentMap[pathlist[i]]]
        cur_cap = matrix[parent][node]
        if cur_cap < bottleneck:
            bottleneck = cur_cap
    #print(pathlist)
    #print(bottleneck)
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
#
print(sum_pos-maxflow)

