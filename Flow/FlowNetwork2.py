import sys
from collections import deque
#{'s': {('2', '10'), ('1', '10')}, '1': {('4', '8'), ('2', '2'), ('3', '4')}, '2': {('4', '9')}, '3': {('t', '10')}, '4': {('t', '10'), ('3', '6')}, 't': set()}

#{'s': {('1', '10'), ('2', '10')}, '1': {('3', '4'), ('4', '8'), ('2', '2')}, '2': {('4', '9')}, '3': {('t', '10')}, '4': {('3', '6'), ('t', '10')}, 't': set()}

#
edges = []
class Edge:
    def __init__(self, v_out, v_in, c, f):
        self.c = c
        self.f = f
        self.v_out = v_out
        self.v_in = v_in

residualgraph = {}
m = int(input())

for i in range(m):
     s = str(input())
     residualgraph[s] = []

n = int(input())

for i in range(n):
    v_out, v_in, c = str(input()).split(" ")
    #edges.append(Edge(v_out, v_in, c, 0))
    residualgraph[v_out].append((v_in, c, 0))

graph = residualgraph
caps = []
path = []
pathwith = []
def dfs(graph, start, bottleneck, visited=None):  #nakket fra https://www.programiz.com/dsa/graph-dfs
    if visited is None:
        visited = []
   # print("Adding v: ", start)
    visited.append(start)

   # print(start)
    path.append(start)
    isForward = True


    for next in graph[start] - visited:
        #print("For, ", next[0], "in ", graph[start], " run dfs")
        caps.append(int(next[1]))
        pathwith.append((start, next[0], next[1], isForward))
        bottleneck = min(bottleneck, int(next[1]))
        #print("bottlenex", bottleneck)

        dfs(graph, next[0], bottleneck, visited)

        return visited, bottleneck

print("residualgraph", residualgraph)
print("graph", graph)
P, bottleneck = dfs(residualgraph, "s", 99999999)
bneck = min(caps)

print("pathwith", pathwith)
print("P", P)
print("bottleneck", bneck)
print("caps", caps)
print("path", path)

def augment(P):
    print("augment:")
    b = int(bneck)
    for i in range(len(P)):
        #print("forlooå")
        if P[i][3]:
            sourcenode = P[i][0]
            print("sourcenode", sourcenode)
            temp = graph.get(sourcenode)
            print(temp)
    print("graph after augment", graph)

augment(pathwith)










