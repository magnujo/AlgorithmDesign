import sys
from collections import deque
import numpy as np

vertices_indices = {}
edges = []
adj = {}
edges.append([None])
m = int(input())
global terminal
global source
global bottleneck

for j in range(m):
    s = str(input())
    edges[0].append(s)
    vertices_indices[s] = int(j + 1)

for i in range(1, m+1):
    s = edges[0][i]
    #print(s)
    edges.append([s])
    #print(edges)
    for v in range(m):
        #print(v)
        edges[i].append(None)

n = int(input())


for i in range(n):
   v_out, v_in, c = str(input()).split(" ")
   row = vertices_indices.get(v_out)
   col = vertices_indices.get(v_in)
   edges[row][col] = c
   if v_out not in adj:
       adj[v_out] = [v_in]
   else:
       adj.get(v_out).append(v_in)

adj['t'] = []


def printMatrix(matrix, spacingfactor=6):
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



#print(np.array(edges))
printMatrix(edges, 7)
print(adj)
print(vertices_indices)

#print(vertices_indices.get("s"))

#print(deque([1,2,3]).pop())

def dfs(startV):
    stack = deque([])
    visited = set()
    stack.append(startV)
    t_reached = False
    path = []
    while len(stack) > 0:

        curr = stack.pop()

        if curr not in visited:
            visited.add(curr)
            print("current node", curr)

        if curr == 't':
            break;

        a = adj[curr]

        print("adjacent nodes", a)

        for i in range(len(a)):
            if a[i] not in visited:
                stack.append(a[i])
        print("stack", stack)
    return visited

print(dfs('s'))







