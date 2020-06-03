file = open("rosalind_ps.txt", "r")
lines = []
for line in file.readlines():
    lines.append(line)

arr = sorted([int(i) for i in lines[1].split()])
num = int(lines[2])
output = ""
for i in range(num):
    if output != "":
        output = output + " "
    output = output + str(arr[i])
print(output, end = "")