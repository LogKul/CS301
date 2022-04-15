# Assignment 5: Sorting Lists, by Logan Kulesus
# Due April 3rd, 2022


# Insertion sort
# O(N^2) running time, because for all N elements of the input list, the code will run through
# each element of the output list. The insert method runs in O(N) time, but runs only if the
# correct index is found within the while loop, so the runtime of the while loop and the
# insert method are additive, not multiplicative, which is why the runtime is O(N^2).


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
# O(N^2) running time, because for every N, the code runs through
# N + (N-1)(N-2)/2 iterations of a few operations, which multiplies out to be O(N^2).


def bubbleSort(li):
    for i in range(0, len(li)):
        for j in range(1, len(li) - i):
            if (li[j] < li[j-1]):
                temp = li[j-1]
                li[j-1] = li[j]
                li[j] = temp


# Selection Sort
# O(N^2) running time, because for each element N of our input list, we run through
# the rest of our list (incrementally, because after each run of the outer for loop,
# the number of times the inner for loop runs decreases by 1), which indicates a
# pattern of runtimes similar to the bubble sort, which involves triangular numbers,
# which resolves to O(N^2).


def selectionSort(li):
    for i in range(0, len(li)):
        min = i
        for j in range(i, len(li)):
            if li[j] < li[min]:
                min = j
        temp = li[min]
        li[min] = li[i]
        li[i] = temp


def selectionSortMax(li):
    for i in range(len(li)-1, -1, -1):
        max = i
        for j in range(0, i):
            if li[j] > li[max]:
                max = j
        temp = li[max]
        li[max] = li[i]
        li[i] = temp


# Merge Sort
# O(N*log(N)) running time, because we break the initial list in half, and divide
# each subsequent list by half as well until each list is length 1, and because
# of the use of recursion, all our broken lists float back up the the initial
# method call while being sorted each time, and with each sort going back up the
# chain. These "sorts" are fast because we are incrementing through the combined
# length of each list, which is O(N), and because of the methodology of halving
# each list, each O(N) "half" of runtime floats all the way back to the top, roughly
# doubling in size each time, which ends up being logarithmic.


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
