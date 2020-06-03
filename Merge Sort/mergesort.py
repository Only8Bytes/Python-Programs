def mergesorted(arr1, arr2):
    result = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    result = result + arr1[i:] + arr2[j:]
    return result

def mergesort(mylist):
    n = len(mylist)
    if n > 1:
        #split
        mid = round(n/2)
        left = mylist[:mid]
        right = mylist[mid:]
        left = mergesort(left)
        right = mergesort(right)
        return mergesorted(left, right)
    else:
        return mylist

file = open("rosalind_ms.txt", "r")
lines = []
for line in file.readlines():
    lines.append(line)
result = mergesort([int(i) for i in lines[1].split()])
ans = ""
for i in result:
    if ans != "":
        ans = ans + " "
    ans = ans + str(i)
print(ans, end = "")