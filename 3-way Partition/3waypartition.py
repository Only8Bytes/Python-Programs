def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

def Partition(arr, left, right):
    x = arr[left]
    m1 = left
    m2 = right
    i = m1
    while i <= m2:
        if arr[i] < x:
            swap(arr, m1 ,i)
            m1 += 1
        elif arr[i] > x:
            swap(arr, m2, i)
            m2 -= 1
            i -= 1
        i += 1
    return m1, m2

file = open("rosalind_par3.txt", "r")
lines = []
for line in file.readlines():
    lines.append(line)
arr = [int(i) for i in lines[1].split()]
numVals = int(lines[0])
Partition(arr, 0, numVals - 1)
ans = ""
for x in arr:
    if ans != "":
        ans = ans + " "
    ans = ans + str(x)
print(ans, end = "")