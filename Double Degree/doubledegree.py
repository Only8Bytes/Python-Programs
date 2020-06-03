neighbors = {}

file = open("rosalind_ddeg.txt", "r")
lines = []
for line in file.readlines():
    lines.append(line)

for i, line in enumerate(lines):
    if i > 0:
        vals = line.split()
        for x in vals:
            if x not in neighbors:
                neighbors[x] = []
            for y in vals:
                if y != x and y not in neighbors[x]:
                    neighbors[x].append(y)

keys = list(neighbors.keys())
for i in range(0, len(keys)):
    keys[i] = int(keys[i])
keys = sorted(keys)
output = ""
for key in keys:
    if output != "":
        output = output + " "
    count = 0
    for neighbor in neighbors[str(key)]:
        count += len(neighbors[str(neighbor)])
    output = output + str(count)

print(output, end = "")