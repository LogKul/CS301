# Insertion sort
# O(N) running time, because


def insertionSort(li):
    outputlist = [li.pop(0)]

    for item in li:
        i = 0
        flag = False
        while (not flag):
            if i == len(outputlist):
                outputlist.append(item)
                flag = True
            elif item < outputlist[i]:
                outputlist.insert(i, item)
                flag = True
            else:
                i += 1
    return outputlist


# Bubble Sort
# O(N) running time, because


def bubbleSort(li):
    for i in range(0, len(li)):
        for j in range(1, len(li) - i):
            if (li[j] < li[j-1]):
                temp = li[j-1]
                li[j-1] = li[j]
                li[j] = temp


# Selection Sort
# O(N) running time, because


def selectionSort(li):
    for i in range(0, len(li)):
        min = i
        for j in range(i, len(li)):
            if li[j] < li[min]:
                min = j
        temp = li[min]
        li[min] = li[i]
        li[i] = temp


# Merge Sort
# O(N) running time, because


def mergeSort(li):
    # Base case, if list has length 1, it is already sorted
    if len(li) > 1:
        # Calculate middle index, and split input list into two smaller lists, L and R
        mid = len(li) // 2
        L = li[:mid]
        R = li[mid:]

        # Call mergeSort for both of the smaller lists
        mergeSort(L)
        mergeSort(R)

        # Begin sorting after sorted contents float back up the recursion ladder from our mergeSort call
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


if __name__ == '__main__':
    # Initialize the lists
    a = [26, 54, 93, 17, 77, 31, 44, 55, 20]
    b = [26, 54, 93, 17, 77, 31, 44, 55, 20]
    c = [26, 54, 93, 17, 77, 31, 44, 55, 20]
    d = [26, 54, 93, 17, 77, 31, 44, 55, 20]

    # Test each sorting function based on initialized lists a, b, c, and d
    print("Unsorted List:  ", a)
    a = insertionSort(a)
    print("Insertion Sort: ", a)
    bubbleSort(b)
    print("Bubble Sort:    ", b)
    selectionSort(c)
    print("Selection Sort: ", c)
    mergeSort(d)
    print("Merge Sort:     ", d)
