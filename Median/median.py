file = open("rosalind_med.txt", "r")
lines = []
for line in file.readlines():
    lines.append(line)

k = int(lines[2])
arr = [int(i) for i in lines[1].split()]
arr.sort()
print(arr[k - 1], end = "")