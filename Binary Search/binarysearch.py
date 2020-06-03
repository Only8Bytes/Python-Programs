def binSearch(A, k):
    n = len(A)
    if n == 1 and A[0] != k:
        return -1
    mid = round(n/2)
    if A[mid] == k:
        return mid + 1
    if A[mid] > k:
        return binSearch(A[:mid], k)
    elif A[mid] < k:
        ans = binSearch(A[mid:], k)
        if ans != -1:
            return mid + ans
        else:
            return ans

def main(n, m, A, K):
    output = ""
    for val in K:
        if output != "":
            output = output + " "
        output = output + str(binSearch(A, val))
    return output

file = open("rosalind_bins.txt", "r")
lines = []
for line in file.readlines():
    lines.append(line)
print(main(int(lines[0]), int(lines[1]), [int(i) for i in lines[2].split()], [int(i) for i in lines[3].split()]))