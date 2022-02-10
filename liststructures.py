from operator import index
from re import A


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class Double_Node:
    def __init__(self, val, last):
        self.value = val
        self.next = None
        self.previous = last


class Linked_List:
    def __init__(self):
        self.start = None

    def add(self, item):
        tempnode = self.start
        self.start = Node(item)
        self.start.next = tempnode

    def remove(self, item):
        currnode = self.start
        prevnode = None
        if currnode.value == item:
            if currnode.next is not None:
                self.start = currnode.next
                del currnode
                return "Item removed"
            else:
                self.start = None
                del currnode
                return "Item removed"
        while currnode.next is not None:
            if currnode.value == item:
                tempnode = currnode
                prevnode.next = currnode.next
                del currnode
                return "Item removed"
            else:
                prevnode = currnode
                currnode = currnode.next
        if currnode.value == item:
            tempnode = currnode
            prevnode.next = currnode.next
            del currnode
            return "Item removed"
        raise Exception("NO SUCH ELEMENT")

    def search(self, item):
        currnode = self.start
        while currnode.next is not None:
            if currnode.value == item:
                return True
            currnode = currnode.next
        if currnode.value == item:
            return True
        return False

    def isEmpty(self):
        return self.start == None

    def size(self):
        currnode = self.start
        index = 1
        if self.start == None:
            return 0
        while currnode.next is not None:
            currnode = currnode.next
            index += 1
        return index

    def append(self, item):
        if self.start == None:
            self.start = Node(item)
        else:
            currnode = self.start
            while currnode.next is not None:
                currnode = currnode.next
            currnode.next = Node(item)

    def index(self, item):
        currnode = self.start
        index = 0
        while currnode.next is not None:
            if currnode.value == item:
                return index
            currnode = currnode.next
            index += 1
        if currnode.value == item:
            return index
        raise Exception("NO SUCH ELEMENT")

    def insert(self, pos, item):
        currnode = self.start
        prevnode = None
        size = self.size()
        if pos > size - 1:
            raise Exception("INDEX OUT OF RANGE")
        for i in range(pos + 1):
            if i == pos:
                tempnode = Node(item)
                tempnode.next = prevnode.next
                prevnode.next = tempnode
            else:
                prevnode = currnode
                currnode = currnode.next

    def pop(self, pos=None):
        currnode = self.start
        prevnode = None
        if pos is None:
            if currnode == None:
                raise Exception("LIST IS EMPTY")
            if currnode.next == None:
                tempnode = currnode
                self.start = None
                return tempnode.value
            while currnode.next is not None:
                prevnode = currnode
                currnode = currnode.next
            tempnode = currnode
            prevnode.next = None
            del currnode
            return tempnode.value
        else:
            size = self.size()
            if currnode == None:
                raise Exception("LIST IS EMPTY")
            elif pos > size - 1:
                raise Exception("INDEX OUT OF RANGE")
            if currnode.next == None:
                tempnode = currnode
                self.start = None
                return tempnode.value
            for i in range(pos):
                prevnode = currnode
                currnode = currnode.next
            tempnode = currnode
            prevnode.next = currnode.next
            del currnode
            return tempnode.value

    def printlist(self):
        if self.start is not None:
            currnode = self.start
            elements = str(self.start.value) + " "
            if self.start == None:
                print("No elements")
                return 0
            while currnode.next is not None:
                currnode = currnode.next
                elements = elements + str(currnode.value) + " "
            print(elements)
        else:
            print("None")


class Doubly_Linked_List:
    def __init__(self):
        self.items = []


# --=[ testing ]=--

items = Linked_List()
items.add("Heyman1")
items.append("Heyman3")
items.append("Heyman5")
items.insert(1, "Heyman2")
items.insert(3, "Heyman4")
items.printlist()

print(str(items.pop(4)))
print(str(items.pop(3)))
print(str(items.pop(2)))
print(str(items.pop(1)))
print(str(items.pop(0)))
print(str(items.pop(0)))
