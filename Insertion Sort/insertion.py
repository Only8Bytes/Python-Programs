file = open("rosalind_ins.txt", "r")
lines = []
for line in file.readlines():
    lines.append(line)

count = 0
length = int(lines[0])
arr = [int(i) for i in lines[1].split()]

for i in range(1, length):
    k = i
    while k >= 1 and arr[k] < arr[k - 1]:
        temp = arr[k]
        arr[k] = arr[k - 1]
        arr[k - 1] = temp
        k -= 1
        count += 1

print(count, end = "")