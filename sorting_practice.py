# Initialize the list
a = [26, 54, 93, 17, 77, 31, 44, 55, 20]

# Insertion sort
b = [26, 54, 93, 17, 77, 31, 44, 55, 20]
for i in range(1, len(b)):
    j = i
    while (b[j] < b[j-1]) & (j > 0):
        temp = b[j-1]
        b[j-1] = b[j]
        b[j] = temp
        j -= 1
print("Insertion Sort:", b)

# Bubble Sort
c = [26, 54, 93, 17, 77, 31, 44, 55, 20]
for i in range(0, len(c)):
    for j in range(1, len(c) - i):
        if (c[j] < c[j-1]):
            temp = c[j-1]
            c[j-1] = c[j]
            c[j] = temp
print("Bubble Sort:   ", c)

# Selection Sort
d = [26, 54, 93, 17, 77, 31, 44, 55, 20]
for i in range(len(d)):
    min = 0
    for j in range(len(d) - i):
        if d[j] < d[min]:
            min = j
    temp = d.pop(min)
    d.append(temp)
print("Selection Sort:", d)

# Merge Sort
e = [26, 54, 93, 17, 77, 31, 44, 55, 20]


def mergeSort(li):
    if len(li) > 1:
        mid = len(li) // 2
        L = li[:mid]
        R = li[mid:]

        mergeSort(L)
        mergeSort(R)

        i = 0
        j = 0
        k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                li[k] = L[i]
                i += 1
            else:
                li[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            li[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            li[k] = R[j]
            j += 1
            k += 1


mergeSort(e)
print("Merge Sort:    ", e)
