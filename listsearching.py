# ASSIGNMENT 4: Searching Lists, by Logan Kulesus

# Binary Search Function
# Parameters:
#   list - input list from user
#   searchval - value to search for in list
#
# HashList Class:
# Constructors:
#   length - integer value for length of list to initialize
# Functions:
#   hashfunction(item), returns index that an item would slot into
#   rehash(startindex, item, search), returns rehashed slot for an item, or a boolean for if a given item is found
#   put(item), adds an item to the HashList by finding the index via the hash & rehash functions
#   contains(item), searches for an item in the list using hashing methodology, calls rehash if not found
#   items(), prints out the HashList in a user-readable format

# I don't know what the below import statement is for, probably auto-generated
# Commented it out just in case.
#from re import S


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
            return self.rehash(index, item)

    def rehash(self, startindex, item, search=False):
        index = startindex
        if search == True:
            while (self.elements[index] != item) & (index < self.length - 1):
                index += 1
            if (index + 1 == self.length) & (self.elements[index] != item):
                index = 0
                while (self.elements[index] != item) & (index < item % self.length):
                    index += 1
            if self.elements[index] == item:
                return True
            else:
                return False
        else:
            while (self.elements[index] is not None) & (index < self.length - 1):
                index += 1
            if (index + 1 == self.length) & (self.elements[index] is not None):
                index = 0
                while (self.elements[index] is not None) & (index < item % self.length):
                    index += 1
            if self.elements[index] is None:
                return index
            else:
                return -1

    def put(self, item):
        index = self.hashfunction(item)
        if index < 0:
            raise Exception("ERROR: HashList already full")
        self.elements[index] = item

    def contains(self, item):
        index = item % (self.length)
        if self.elements[index] == item:
            return True
        else:
            return self.rehash(index, item, search=True)

    def items(self):
        output = "[ "
        for i in range(self.length):
            if self.elements[i] != None:
                output = output + str(self.elements[i]) + ", "
        if output != "[ ":
            return output[:-2] + " ]"
        else:
            return "[]"

# 3.) - Running times of the HashList methods in best-case and worst-case
#       -The best-case runtimes of the hashfunction, rehash, put, and contains
#        functions is O(1), because the allocated slot for our data value has
#        no collisions, so we don't need to increment down our list. However,
#        the items function is always O(N) in both best and worst cases,
#        because we iterate through the entire list to print out each data
#        value.
#        For worst case runtimes, our hachfunction, rehash, put, and contain functions
#        are O(N), as in the worst case, there is a collision at every slot up
#        until the slot before the (item's value % list length) best-case slot,
#        which happens because when a slot is occupied with rehashing by linear
#        probing, the next adjacent slot is checked, up until the end of the list
#        is reached, and the function loops back to the start to keep checking for
#        slots up until the original designated slot is reached. So, in the worst
#        case, our rehashing function searches through the list in N operations in the worst
#        case, which is O(N). The put and contains functions either use the
#        hashfunction or use a method similar to that of the hashfunction, which uses
#        the rehash method which has a worst-case runtime of O(N), so they
#        also have a worst-case runtime of O(N).
#
# 4.) - How a HashList needs to be modified to convert it into a dictionary
#       -In order to convert a HashList into a dictionary, and thus achieve a
#        runtime of O(1) with no collisions whatsoever, we need to have keys rather
#        than numerically ordered slots. With hashing, we try to map input values to
#        pre-generated slot values, but with dictionaries, we would need key values
#        to exists as a reference to a slot in memory, or in other words, we would
#        need each key to represent a slot. This means we would need completely
#        different methods, as well as needing to manage keys and the values they
#        are paired with, rather than just the values.


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
print(a.contains(1))
print(a.contains(2))
print(a.contains(27))
print(a.contains(4))
print(a.contains(5))
print(a.contains(6))
print(a.contains(7))
print(a.contains(8))
print(a.contains(9))
print(a.contains(10))
print(a.contains(90))
