a = [4, 5, 6, 2, 1]
for i in range(len(a)-1):
    for j in range(i+1, len(a)-1):
        if a[i] > a[j]:
            t = a[i]
            a[i] = a[j]
            a[j] = t
print(a)