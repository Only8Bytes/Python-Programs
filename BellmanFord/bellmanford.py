import math
file = open("input.txt", "r")
lines = []
for line in file.readlines():
    lines.append(line)

def bellmanFord(graph, numNodes, numEdges, source):
    distances = [math.inf] * numNodes
    distances[int(source) - 1] = 0
    for i in range(numNodes - 1):
        for node in graph:
            for edge in graph[node]:
                #key = edge, cost = graph[node][edge]
                weight = graph[node][edge]
                if distances[int(node) - 1] != math.inf and distances[int(node) - 1] + weight < distances[int(edge) - 1]:
                    distances[int(edge) - 1] = distances[int(node) - 1] + weight
        
    for node in graph:
        for edge in graph[node]:
            if distances[int(node) - 1] != math.inf and distances[int(node) - 1] < distances[int(edge) - 1]:
                return None

    return distances


vals = lines[0].split()
numNodes = int(vals[0])
numEdges = int(vals[1])
neighbors = {}
for i in range(1, numNodes + 1):
    neighbors[str(i)] = {}
for i, line in enumerate(lines):
    if i > 0:
        vals = line.split()
        if vals[1] not in neighbors[vals[0]]:
            neighbors[vals[0]][vals[1]] = int(vals[2])

result = bellmanFord(neighbors, numNodes, numEdges, "1")
ans = ""
if result != None:
    for val in result:
        if ans != "":
            ans = ans + " "
        if val == math.inf:
            ans = ans + "x"
        else:
            ans = ans + str(val)
print(ans, end = "")