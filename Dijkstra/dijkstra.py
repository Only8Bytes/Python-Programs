import math
file = open("rosalind_dij.txt", "r")
lines = []
for line in file.readlines():
    lines.append(line)

def dijkstra(graph, source, n):
    distances = {}
    visited = []
    unvisited = []
    for i in range(1, n + 1):
        distances[str(i)] = math.inf
        unvisited.append(str(i))
    distances["1"] = 0
    while unvisited:
        node = unvisited.pop(0)
        if node not in visited:
            visited.append(node)
            for newNode in graph[node]:
                if distances[node] + graph[node][newNode][0] < distances[newNode]:
                    distances[newNode] = distances[node] + graph[node][newNode][0]
        unvisited = [x for x in sorted(distances, key = distances.__getitem__)]
        for x in visited:
            if x in unvisited:
                unvisited.remove(x)

    return distances



vals = lines[0].split()
numNodes = int(vals[0])
neighbors = {}
for i in range(1, numNodes + 1):
    neighbors[str(i)] = {}
for i, line in enumerate(lines):
    if i > 0:
        vals = line.split()
        if vals[1] not in neighbors[vals[0]]:
            neighbors[vals[0]][vals[1]] = [int(vals[2])]

result = dijkstra(neighbors, "1", numNodes)
ans = ""
for i in range(1, numNodes + 1):
    val = result[str(i)]
    if ans != "":
        ans = ans + " "
    if val == math.inf:
        ans = ans + "-1"
    else:
        ans = ans + str(val)
print(ans, end = "")