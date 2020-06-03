def mostOccurring(mylist):
    res = max(set(mylist), key = mylist.count)
    return [res, mylist.count(res)]

file = open("rosalind_maj.txt", "r")
lines = []
for line in file.readlines():
    lines.append(line)

output = ""
vals = lines[0].split()
min = int(vals[1])/2
for i, v in enumerate(lines):
    if i >= 1:
        if output != "":
            output = output + " "
        result = mostOccurring([int(i) for i in v.split()])
        if result[1] >= min:
            output = output + str(result[0])
        else:
            output = output + "-1"
print(output, end = "")