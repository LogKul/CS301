# ASSIGNMENT 4: Searching Lists, by Logan Kulesus

# Binary Search Function
# Parameters:
#   list - input list from user
#   searchval - value to search for in list
from re import S


def search_sorted_list(sorted_list, item):
    return bin_search(sorted_list, item, 0, len(sorted_list)-1)


def bin_search(sorted_list, item, first_index, last_index):
    if last_index - first_index >= 0:
        mid_index = (last_index + first_index) // 2
        if item < sorted_list[mid_index]:
            return bin_search(sorted_list, item, first_index, mid_index - 1)
        elif item > sorted_list[mid_index]:
            return bin_search(sorted_list, item, mid_index + 1, last_index)
        elif item == sorted_list[mid_index]:
            return True
    else:
        print("not found")
        return False


# HashList class
class HashList:

    def __init__(self, length):
        self.elements = [None] * length
        self.length = length

    def hashfunction(self, item):
        index = item % (self.length)
        if self.elements[index] is None:
            return index
        else:
            while (self.elements[index] is not None) & (index < self.length - 1):
                index += 1
            if (index + 1 == self.length) & (self.elements[index] is not None):
                index = 0
                while (self.elements[index] is not None) & (index < item % self.length):
                    index += 2
            if self.elements[index] is None:
                return index
            else:
                raise Exception("ERROR: HashList already full")

    def put(self, item):
        self.elements[self.hashfunction(item)] = item

    def contains(self, item):
        for i in range(self.length):
            if self.elements[i] == item:
                return True
        return False

    def items(self):
        output = "[ "
        for i in range(self.length):
            if self.elements[i] != None:
                output = output + str(self.elements[i]) + ", "
        if output != "[ ":
            return output[:-2] + " ]"
        else:
            return "[]"


a = HashList(10)
a.put(1)
a.put(2)
a.put(27)
a.put(4)
a.put(5)
a.put(6)
a.put(7)
a.put(8)
print(a.items())
a.put(9)
a.put(10)
print(a.items())
