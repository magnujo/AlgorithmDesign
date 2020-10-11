# 4 3 1 <- [number of children, number of toys, number of toy categorise]
# 2 1 2 <- [Number of different toys that satisfy, Toys...]
# 2 1 2 <- ...
# 1 3
# 1 3
# 2 1 2 1 <- Category discriprtion = [number of toys in category, toys in category..., max toys to be used]
# in the above category there are 2 toys but there 3 toys in total? Can a toy be used if its not in a category?
# What does it mean that at most 1 toy can be used?
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
matrix = []
residualmatrix = []
matrix.append([0])
matrix[0].append('s')
matrix.append(['s'])
indexes['s'] = index
index = index + 1
matrixSize = int(numofchildren) + int(numoftoys) + int(numofcat) + 2

for i in range(matrixSize):
    if 0 < i <= int(numofchildren):
        matrix[1].append(1)
    else:
        matrix[1].append(0)

#print("num of children:", numofchildren)
#print("num of toys:", numoftoys)
#print("num of categories:", numofcat)
#print("Matrix size:", matrixSize)


for i in range(int(numofchildren)):
    num = 'b' + str(i+1)
    matrix[0].append(num)
    indexes[num] = index
    index = index + 1

for i in range(int(numoftoys)):
    num = 't' + str(i+1)
    matrix[0].append(num)
    indexes[num] = index
    index = index + 1

for i in range(int(numofcat)):
    num = 'c' + str(i+1)
    matrix[0].append(num)
    indexes[num] = index
    index = index + 1

matrix[0].append('t')
indexes['t'] = index
index = index + 1

for i in range(int(numofchildren)):
    k_idx = 1
    v_name = 'b' + str(i+1)
    matrix.append([v_name])
    k = input().split()

    for j in range(matrixSize):

        if k_idx == len(k):
            matrix[i + 2].append(0)
        elif matrix[0][j+1] == 't'+k[k_idx]:
            matrix[i+2].append(1)
            k_idx = k_idx + 1
        else:
            matrix[i+2].append(0)


for i in range(int(numoftoys)):
    v_name = 't' + str(i+1)
    matrix.append([v_name])
    for j in range(matrixSize-1):
        matrix[i+int(numofchildren)+2].append(0)
    matrix[i + int(numofchildren) + 2].append(1)


for i in range(int(numofcat)):
   # print("i", i)
    k = input().split()
    v_name = 'c' + str(i+1)
    k_len = len(k)
    matrix.append([v_name])
    c_out = k[k_len-1]
   # print("c_out", c_out)
    for j in range(int(k[0])):
        idx_row = 1 + int(numofchildren) + int(k[j+1])
        idx_col = 1 + int(numoftoys) + int(numofchildren) + i + 1
        matrix[idx_row][idx_col] = 1
        matrix[idx_row][matrixSize] = 0
    for k in range(matrixSize):
        if matrix[0][k+1] == 't':
            matrix[i + 2 + int(numoftoys) + int(numofchildren)].append(c_out)
        else:
            matrix[i + 2 + int(numoftoys) + int(numofchildren)].append(0)

matrix.append(['t'])

for i in range(matrixSize):
    matrix[matrixSize].append(0)


residualmatrix = matrix
bottleneck = 1
def dfs(startV):
    t_reached = False
    pathlist = []
    stack = deque([])
    visited = set()
    stack.append(startV)
    t_reached = False
    while len(stack) > 0:

        currentnode = stack.pop()
        currentnodeindex = indexes[currentnode]

        if currentnode not in visited:
            visited.add(currentnode)
            #print("current node", currentnode)
        pathlist.append(currentnode)
        if currentnode == 't':
            t_reached = True
            break

        for i in range(1, len(matrix[currentnodeindex])):
            if matrix[0][i] not in visited and int(matrix[currentnodeindex][i]) > 0:
                stack.append(matrix[0][i])
        #print("stack", stack)
    return pathlist, t_reached

maxflow = 0
treached = True
#printMatrix(matrix)
#print(indexes)

while treached:
    #print("hej")
    pathlist, treached = dfs(('s'))
    if treached:
        maxflow = maxflow + bottleneck
    #print("pathlist", pathlist)
    #print("treached", treached)
    for i in range(len(pathlist) - 1):
        row_idx = indexes[pathlist[i]]
        col_idx = indexes[pathlist[i + 1]]
        matrix[row_idx][col_idx] = 0
    #printMatrix(matrix)


print(maxflow)