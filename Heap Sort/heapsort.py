def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        swap(arr, i, largest)
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    mid = round(n/2)
    for i in range(mid - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        swap(arr, i, 0)
        heapify(arr, i, 0)

file = open("rosalind_hs.txt", "r")
lines = []
for line in file.readlines():
    lines.append(line)

arr = [int(i) for i in lines[1].split()]
heapSort(arr)
ans = ""
for i in arr:
    if ans != "":
        ans = ans + " "
    ans = ans + str(i)
print(ans, end = "")