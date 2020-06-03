def Partition(arr, left, right):
    i = left - 1
    pivot = arr[right]
    for x in range(left, right):
        if arr[x] <= pivot:
            i += 1
            temp = arr[i]
            arr[i] = arr[x]
            arr[x] = temp
    temp = arr[right]
    arr[right] = arr[i + 1]
    arr[i + 1] = temp
    return i + 1

def QuickSort(arr, left, right):
    if left < right:
        index = Partition(arr, left, right)
        QuickSort(arr, left, index - 1)
        QuickSort(arr, index + 1, right)

file = open("rosalind_qs.txt", "r")
lines = []
for line in file.readlines():
    lines.append(line)
arr = [int(i) for i in lines[1].split()]
QuickSort(arr, 0, len(arr) - 1)
ans = ""
for i in arr:
    if ans != "":
        ans = ans + " "
    ans = ans + str(i)
print(ans, end = "")