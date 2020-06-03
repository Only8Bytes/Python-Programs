import math

def BFS(graph, numNodes, numEdges, start, goal):
    if start == goal:
        return 0
    distances = [math.inf] * numNodes
    preds = {}
    visited = [False] * numNodes
    queue = [start]
    visited[int(start) - 1] = True
    distances[int(start) - 1] = 0
    while queue:
        node = queue.pop(0)
        if node in graph:
            for i in graph[node]:
                if not visited[int(i) - 1]:
                    visited[int(i) - 1] = True
                    distances[int(i) - 1] = distances[int(node) - 1] + 1
                    preds[i] = node
                    queue.append(i)
                    if i == goal:
                        length = 0
                        curr = i
                        while curr in preds:
                            length += 1
                            curr = preds[curr]
                        #backtrack
                        return length
    return -1

file = open("rosalind_bfs.txt", "r")
lines = []
for line in file.readlines():
    lines.append(line)
vals = lines[0].split()
numNodes = int(vals[0])
numEdges = int(vals[1])

neighbors = {}
for i, line in enumerate(lines):
    if i > 0:
        vals = line.split()
        x = str(vals[0])
        y = str(vals[1])
        if x not in neighbors:
            neighbors[x] = []
        neighbors[x].append(y)

output = ""
for i in range(numNodes):
    ans = BFS(neighbors, numNodes, numEdges, "1", str(i + 1))
    if output != "":
        output = output + " "
    output = output + str(ans)

print(output, end = "")