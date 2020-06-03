file = open("input.txt", "r")
lines = []
for line in file.readlines():
    lines.append(line)

def sort(graph, v, visited, stack):
    visited[v - 1] = True
    if str(v) in graph:
        for i in graph[str(v)]:
            if not visited[int(i) - 1]:
                sort(graph, int(i), visited, stack)
    stack.insert(0, v)

def topologicalSort(graph, n):
    visited = [False] * n
    stack = []
    for i in range(1, n + 1):
        if not visited[i - 1]:
            sort(graph, i, visited, stack)
    return stack

neighbors = {}
for i in range(1, len(lines)):
    vals = lines[i].split()
    if vals[0] not in neighbors:
        neighbors[vals[0]] = []
    if vals[1] not in neighbors[vals[0]]:
        neighbors[vals[0]].append(vals[1])

vals = lines[0].split()
numNodes = int(vals[0])
result = topologicalSort(neighbors, numNodes)
ans = ""
for v in result:
    if ans != "":
        ans = ans + " "
    ans = ans + str(v)
print(ans, end = "")