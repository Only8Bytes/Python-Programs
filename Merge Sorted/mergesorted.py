file = open("rosalind_mer.txt", "r")
lines = []
for line in file.readlines():
    lines.append(line)
arr1 = [int(i) for i in lines[1].split()]
arr2 = [int(i) for i in lines[3].split()]
i = 0
j = 0

result = []
while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        result.append(arr1[i])
        i += 1
    else:
        result.append(arr2[j])
        j += 1

result = result + arr1[i:] + arr2[j:]
ans = ""
for i in result:
    if ans != "":
        ans = ans + " "
    ans = ans + str(i)
print(ans, end = "")