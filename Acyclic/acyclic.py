file = open("rosalind_dag.txt", "r")
lines = []
for line in file.readlines():
    lines.append(line)
numGraphs = int(lines[0])

output = ""

def Cycles(graph):
    visited = []
    queue = ["1"]
    while queue:
        node = queue.pop(0)
        if node in visited:
            return True
        visited.append(node)
        for newNode in graph[node]:
            queue.append(newNode)
    return False

lineNum = 2
for i in range(numGraphs):
    neighbors = {}
    lineOne = False
    nodes = 0
    while lineNum < len(lines) and len(lines[lineNum]) > 1:
        vals = lines[lineNum].split()
        if nodes == 0:
            nodes = int(vals[0])
            for i in range(1, nodes + 1):
                neighbors[str(i)] = []
        else:
            if vals[1] not in neighbors[vals[0]]:
                neighbors[vals[0]].append(vals[1])
        lineNum += 1
    lineNum += 1
    if output != "":
        output = output + " "
    if not Cycles(neighbors):
        output = output + "1"
    else:
        output = output + "-1"
print(output, end = "")