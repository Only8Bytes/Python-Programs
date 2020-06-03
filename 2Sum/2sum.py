import math
def sum2(mylist):
    result = (math.inf, math.inf)
    for i, v in enumerate(mylist):
        if mylist[i + 1:].count(v * -1) > 0:
            if i < mylist.index(v * -1, i + 1) and mylist.index(v * -1, i + 1) < result[1]:
                result = (i, mylist.index(v * -1, i + 1))
    if result == (math.inf, math.inf):
        return -1
    else:
        return result

file = open("rosalind_2sum.txt", "r")
lines = []
for line in file.readlines():
    lines.append(line)
for i, v in enumerate(lines):
    if i >= 1:
        arr = [int(i) for i in v.split()]
        if i >= 2:
            print("")
        result = sum2([int(i) for i in v.split()])
        if result == -1:
            print(-1, end = "")
        else:
            print(str(result[0] + 1) + " " + str(result[1] + 1), end = "")