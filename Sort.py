a = [10, 20, 70, 90, 60, 30, 40]

for i in range(len(a)):
    low = i
    for v in range(i + 1, len(a)):
        if a[v] < a[low]:
            low = v
    a[i], a[low] = a[low], a[i]

print(a)
