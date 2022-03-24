# Initialize the list
a = [26, 54, 93, 17, 77, 31, 44, 55, 20]

# Insertion sort
b = a
for i in range(1, len(b)):
    j = i
    while (b[j] < b[j-1]) & (j > 0):
        temp = b[j-1]
        b[j-1] = b[j]
        b[j] = temp
        j -= 1
print("Insertion Sort:", b)

# Bubble Sort
c = a
for i in range(1, len(c)):
    for j in range(1, len(c) - i):
        if (c[j] < c[j-1]):
            temp = c[j-1]
            c[j-1] = c[j]
            c[j] = temp
print("Bubble Sort:   ", c)

# Selection Sort
d = a
for i in range(len(d)):
    min = 0
    for j in range(len(d) - i):
        if d[j] < d[min]:
            min = j
    temp = d.pop(min)
    d.append(temp)
print("Selection Sort:", d)

# Merge Sort
e = a
