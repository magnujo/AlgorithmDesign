import sys
from collections import deque
import numpy as np







vertices = {}
edges = []
edge_indices = {}
#edges.append([None])


#print(np.array(edges))
edges.append([None])
m = int(input())

for j in range(m):
    s = str(input())
    edges[0].append(s)
    vertices[s] = int(j+1)

#print(edges)


for i in range(1, m+1):
    s = edges[0][i]
    #print(s)
    edges.append([s])
    print(edges)
    for v in range(m):
        print(v)
        edges[i].append(0)





print(np.array(edges))
print(vertices)

n = int(input())
print(n)
#
for i in range(n):
   v_out, v_in, c = str(input()).split(" ")
   row = vertices.get(v_out)
   col = vertices.get(v_in)
   edges[row][col] = c

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



print(np.array(edges))
printMatrix(edges, 7)



# graph = residualgraph
# caps = []
# path = []
# pathwith = []
# def dfs(graph, start, bottleneck, visited=None):  #nakket fra https://www.programiz.com/dsa/graph-dfs
#     if visited is None:
#         visited = set()
#     print("Adding v: ", start)
#     visited.add(start)
#
#     print(start)
#     path.append(start)
#     isForward = True
#
#
#     for next in graph[start] - visited:
#        # print("For, ", next[0], "in ", graph[start], " run dfs")
#         caps.append(int(next[1]))
#         pathwith.append((start, next[0], next[1], isForward))
#         bottleneck = min(bottleneck, int(next[1]))
#         print("bottlenex", bottleneck)
#
#         dfs(graph, next[0], bottleneck, visited)
#
#         return visited, bottleneck
#
# print(residualgraph)
# P, bottleneck = dfs(residualgraph, "s", 99999999)
# bneck = min(caps)
#
# print("pathwith", pathwith)
# print("P", P)
# print("bottleneck", bneck)
# print("caps", caps)
# print("path", path)
#
#








