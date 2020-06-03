neighbors = {}

class Set():
    def __init__(self):
        self.Parent = None

    def getRoot(self):
        if self.Parent is None:
            return self
        return self.Parent.getRoot()

    def union(self, other):
        otherRoot = other.getRoot()
        selfRoot = self.getRoot()
        if selfRoot != otherRoot:
            selfRoot.Parent = otherRoot

file = open("rosalind_cc.txt", "r")
lines = []
for line in file.readlines():
    lines.append(line)

vals = lines[0].split()
numKeys = int(vals[0])
for i in range(1, numKeys + 1):
    neighbors[str(i)] = []

for i, line in enumerate(lines):
    if i > 0:
        vals = line.split()
        for x in vals:
            for y in vals:
                if y != x and y not in neighbors[x]:
                    neighbors[x].append(y)

keys = list(neighbors.keys())
components = 0
sets = {}
for key in keys:
    sets[key] = Set()
for key in keys:
    for neighbor in neighbors[key]:
        sets[key].union(sets[neighbor])
components = len(set(x.getRoot() for x in sets.values()))

print(components, end = "")