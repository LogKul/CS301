from operator import index
from re import A


# ===== Stack Class =====
class Stack:
    # Basic stack class, last in, first out
    def __init__(self):
        self.items = []

    # Returns boolean if stack is empty or not
    # O(1)
    def isEmpty(self):
        return self.items == []

    # Place item onto stack
    # O(1)
    def push(self, item):
        self.items.append(item)

    # Remove and return element on top of stack
    # O(1)
    def pop(self):
        return self.items.pop()

    # Return the value of the current item at top of stack
    # O(1)
    def peek(self):
        return self.items[len(self.items)-1]

    # Returns number of elements in stack
    # O(1)
    def size(self):
        return len(self.items)

    # Prints all elements of stack
    def printStack(self):
        print(self.items)


# ===== Queue Class =====
class Queue:
    # Queue list structure, first in, first out
    def __init__(self):
        self.items = []

    # Add item to back of queue
    # O(1)
    def enqueue(self, item):
        self.items.append(item)

    # Remove and return element first up in queue
    # O(N)
    def dequeue(self):
        item = self.items[0]
        del self.items[0]
        return item

    # Returns boolean for if list queue is empty or not
    # O(1)
    def isEmpty(self):
        return self.items == []

    # Returns length of queue
    # O(1)
    def size(self):
        return len(self.items)

    # Prints all elements of queue
    def printQueue(self):
        print(self.items)


# ===== Dequeue (Deque) Class =====
class Deque:
    # Dequeue list structure, can act as both a queue and a stack, double-ended
    def __init__(self):
        self.items = []

    # Adds element to front of deque
    # O(N)
    def addFront(self, item):
        self.items.insert(0, item)

    # Adds element to back of deque
    # O(1)
    def addRear(self, item):
        self.items.append(item)

    # Removes and returns element at front of deque
    # O(N)
    def removeFront(self):
        item = self.items[0]
        del self.items[0]
        return item

    # Removes and returns element at back of deque
    # O(1)
    def removeRear(self):
        item = self.items[len(self.items)-1]
        del self.items[len(self.items)-1]
        return item

    # Returns boolean for if deque is empty or not
    # O(1)
    def isEmpty(self):
        return self.items == []

    # Returns number of elements in deque
    # O(1)
    def size(self):
        return len(self.items)

    # Print all elements of deque
    def printDeque(self):
        return print(self.items)


# ===== Node Class =====
class Node:
    # Node class only holds a value, holds reference to next node object, and holds reference to previous node object
    # A value is the only necessary parameter, but reference to previous node object can be passed in, defaults to None
    def __init__(self, val, prev=None):
        self.value = val
        self.next = None
        self.previous = prev


# ===== Linked List =====
class Linked_List:
    # Linked list is initialized with a head node and an element counter
    def __init__(self):
        self.start = None
        self.elements = 0

    # Item parameter is added as the new starting node
    # O(1)
    def add(self, item):
        tempnode = self.start
        self.start = Node(item)
        self.start.next = tempnode
        self.elements += 1

    # Removes item, base cases for if list is empty and if list has only 1 element, returns string signalling removal of item
    # O(N)
    def remove(self, item):
        currnode = self.start
        prevnode = None
        if currnode == None:
            raise Exception("NO SUCH ELEMENT")
        if currnode.value == item:
            self.start = currnode.next
            del currnode
            self.elements -= 1
            return "Item removed"
        while currnode.next is not None:
            prevnode = currnode
            currnode = currnode.next
            if currnode.value == item:
                prevnode.next = currnode.next
                del currnode
                self.elements -= 1
                return "Item removed"
        raise Exception("NO SUCH ELEMENT")

    # Searches for item and returns boolean if item is found or not
    # O(N)
    def search(self, item):
        currnode = self.start
        while currnode is not None:
            if currnode.value == item:
                return True
            currnode = currnode.next
        return False

    # Returns boolean if head node is an element
    # O(1)
    def isEmpty(self):
        return self.start == None

    # Returns element count
    # O(1)
    def size(self):
        return self.elements

    # Adds node to the end of the linked list, base case for when list is empty
    # O(N)
    def append(self, item):
        if self.start == None:
            self.start = Node(item)
        else:
            currnode = self.start
            while currnode.next is not None:
                currnode = currnode.next
            currnode.next = Node(item)
        self.elements += 1

    # Searches for item and returns index if item is found
    # O(N)
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

    # Inserts item at a position in between two elements, has base cases for if insertion position is at the start
    # and for when the position is not in the range of elements
    # O(N)
    def insert(self, pos, item):
        currnode = self.start
        prevnode = None
        size = self.elements
        if pos == 0:
            tempnode = Node(item)
            tempnode.next = currnode
            self.start = tempnode
            self.elements += 1
        elif pos > size or pos < 0:
            raise Exception("INDEX OUT OF RANGE")
        else:
            for i in range(pos + 1):
                if i == pos:
                    tempnode = Node(item)
                    tempnode.next = prevnode.next
                    prevnode.next = tempnode
                    self.elements += 1
                else:
                    prevnode = currnode
                    currnode = currnode.next

    # Deleted element from list and returns its value, has 2 modes with position and without:
    # WITHOUT POSITION: Last element is popped, base cases for if list is empty and if list only has 1 element
    # WITH POSITION: Element at position is popped, 2 surrounding nodes rejoined, base cases for
    #                when list is empty, position is out of range of the list, if list has only 1 element,
    #                and if the head node is being popped
    # O(N)
    def pop(self, pos=None):
        currnode = self.start
        prevnode = None
        if pos is None:
            if currnode == None:
                raise Exception("LIST IS EMPTY")
            if currnode.next == None:
                tempnode = currnode
                self.start = None
                self.elements -= 1
                del currnode
                return tempnode.value
            while currnode.next is not None:
                prevnode = currnode
                currnode = currnode.next
            tempnode = currnode
            prevnode.next = None
            del currnode
            self.elements -= 1
            return tempnode.value
        else:
            size = self.elements
            if currnode == None:
                raise Exception("LIST IS EMPTY")
            elif pos > size - 1 or pos < 0:
                raise Exception("INDEX OUT OF RANGE")
            if currnode.next == None:
                tempnode = currnode
                self.start = None
                self.elements -= 1
                return tempnode.value
            if pos == 0:
                self.start = currnode.next
                tempnode = currnode
                self.elements -= 1
                del currnode
                return tempnode.value
            for i in range(pos):
                prevnode = currnode
                currnode = currnode.next
            tempnode = currnode
            prevnode.next = currnode.next
            del currnode
            self.elements -= 1
            return tempnode.value

    # Function that prints the list, mostly for debugging, base case for is list is empty
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


# ===== Doubly-Linked List =====
class Doubly_Linked_List:
    # Doubly linked list is initialized with a head node and an element counter
    def __init__(self):
        self.start = None
        self.elements = 0

    # Item parameter is added as the new starting node
    # O(1)
    def add(self, item):
        tempnode = Node(item)
        tempnode.next = self.start
        if self.start is not None:
            self.start.previous = tempnode
        self.elements += 1
        self.start = tempnode

    # Removes item, base cases for if list is empty and if list has only 1 element, returns string signalling removal of item
    # O(N)
    def remove(self, item):
        currnode = self.start
        if currnode == None:
            raise Exception("NO SUCH ELEMENT")
        if currnode.value == item:
            self.start = currnode.next
            self.start.previous = None
            self.elements -= 1
            return "Item removed"
        while currnode.next is not None:
            currnode = currnode.next
            if currnode.value == item:
                currnode.previous.next = currnode.next
                self.elements -= 1
                return "Item removed"
        raise Exception("NO SUCH ELEMENT")

    # Searches for item and returns boolean if item is found or not
    # O(N)
    def search(self, item):
        currnode = self.start
        while currnode is not None:
            if currnode.value == item:
                return True
            currnode = currnode.next
        return False

    # Returns boolean whether head node is an element or not
    # O(1)
    def isEmpty(self):
        return self.start == None

    # Returns element counter
    # O(1)
    def size(self):
        return self.elements

    # Adds node to the end of the linked list, base case for when list is empty
    # O(N)
    def append(self, item):
        if self.start == None:
            self.start = Node(item)
        else:
            currnode = self.start
            while currnode.next is not None:
                currnode = currnode.next
            currnode.next = Node(item)
            currnode.next.previous = currnode
        self.elements += 1

    # Searches for item and returns index if item is found
    # O(N)
    def index(self, item):
        currnode = self.start
        index = 0
        while currnode is not None:
            if currnode.value == item:
                return index
            currnode = currnode.next
            index += 1
        raise Exception("NO SUCH ELEMENT")

    # Inserts item at a position in between two elements, has base cases for if insertion position is at the start
    # and for when the position is not in the range of elements
    # O(N)
    def insert(self, pos, item):
        currnode = self.start
        size = self.elements
        if pos == 0:
            self.start = Node(item)
            self.start.next = currnode
            currnode.previous = self.start
            self.elements += 1
        elif pos > size or pos < 0:
            raise Exception("INDEX OUT OF RANGE")
        elif pos == size:
            while currnode.next is not None:
                currnode = currnode.next
            currnode.next = Node(item)
            currnode.next.previous = currnode
            self.elements += 1
        else:
            currnode = currnode.next
            for i in range(1, pos):
                if i == pos - 1:
                    tempnode = Node(item)
                    tempnode.next = currnode.next
                    currnode.next = tempnode
                    tempnode.previous = currnode
                    tempnode.next.previous = tempnode
                    self.elements += 1
                else:
                    currnode = currnode.next

    # Deleted element from list and returns its value, has 2 modes with position and without:
    # WITHOUT POSITION: Last element is popped, base cases for if list is empty and if list only has 1 element
    # WITH POSITION: Element at position is popped, 2 surrounding nodes rejoined, base cases for
    #                when list is empty, position is out of range of the list, if list has only 1 element,
    #                and if the head node is being popped
    # O(N)
    def pop(self, pos=None):
        currnode = self.start
        if pos is None:
            if currnode == None:
                raise Exception("LIST IS EMPTY")
            if currnode.next == None:
                tempnode = currnode
                self.start = None
                self.elements -= 1
                return tempnode.value
            while currnode.next is not None:
                currnode = currnode.next
            currnode.previous.next = None
            self.elements -= 1
            return currnode.value
        else:
            size = self.elements
            if currnode == None:
                raise Exception("LIST IS EMPTY")
            elif pos > size - 1 or pos < 0:
                raise Exception("INDEX OUT OF RANGE")
            elif currnode.next == None:
                self.start = None
                self.elements -= 1
                return currnode.value
            elif pos == 0:
                self.start = currnode.next
                self.start.previous = None
                self.elements -= 1
                return currnode.value
            else:
                for i in range(pos):
                    currnode = currnode.next
                currnode.previous.next = currnode.next
                self.elements -= 1
                return currnode.value

    # Function that prints the list, mostly for debugging, base case for is list is empty
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


# --=[ TESTING ]=--

if __name__ == "__main__":
    items = Doubly_Linked_List()
    items.add("Heyman2")
    items.printlist()
    items.append("Heyman3")
    items.printlist()
    items.insert(2, "Heyman5")
    items.printlist()
    items.insert(0, "Heyman1")
    items.printlist()
    items.insert(3, "Heyman4")
    items.printlist()

    print(items.pop())
    print(items.pop())
    print(items.pop())

    items.printlist()


# ===== Assignment Questions =====

# 6.)   Q.) Do you think that python’s internal representation of a list is a linked-list, a doubly-linked list,
#           or something else? Why or why not?
#
#       A.) I think that while a lot of Linked-List operations seem to have similar O(N) runtimes to lists,
#           but in reverse, as Linked Lists are faster from the start of the list while Python lists are
#           faster from the end.I think that lists must be something else entirely different because of
#           the constant time to find the value of an element at an index. There are probably many different ways
#           to add functionality to a Linked List to change runtimes of specific functions, like the size()
#           function for example which saves an internal representation of the Linked List size and
#           modifies it each time a Node is added/removed. However, I do not think it would be possible
#           to have O(1) runtime to find the value at an index with either Linked Lists or Doubly Linked
#           Lists, so I don't know what the default list structure in Python is. However, it definitely
#           could be possible that Python uses Linked Lists and I just don't understand how, but another
#           thing to note is that Doubly-Linked Lists seem to have the same runtimes as Linked Lists, so
#           in terms of runtime, they are very similar with Doublies having slightly higher constant
#           runtimes per element N being operated with, which doesn't affect the Big Oh runtime.
#
# 7.)   Q.) Now that you’ve implemented linked lists and doubly-linked lists, you have the option of
#           using these in place of python lists inside your implementation of stacks, queues, and dekes.
#           For each of these, explain which type of list(python list, linked list, or doubly-linked list)
#           should give the best Big Oh running time in a comment.
#
#       A.) To start off, I believe that list structures each have their own use, and with different Big Oh
#           runtimes for different functions, the data structure with the "best Big Oh running time" would
#           be contextually dependent on which functions need to be used more. However, to answer the actual
#           question, we will look for which function seems to have the lowest overall Big Oh runtimes of all
#           data structure methods. And so it would seem that Stacks are the fastest, with averages Big Oh
#           runtimes of O(1), and seemingly only runtimes of O(1). However, Stacks are clearly not the most
#           useful or versatile data structures, so just because it's faster does not mean it's the best.
#
