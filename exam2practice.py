def fA(ulist):
    slist = []
    for k in range(len(ulist)):
        item = ulist[k]
        l = 0
        for l in range(len(slist)):
            if item > slist[l]:
                l += 1
                print('incrementing l', l)
            else:
                print('breaking loop')
                break
        print('inserting', item, 'into', l)
        slist.insert(l, item)
    return slist


def binarysearch(sorted_list, item):
    found = binRecur(sorted_list, item, 0, len(sorted_list)-1)
    return found


def binRecur(l, item, li, ri):
    if ri-li >= 0:
        mid = (ri + li) // 2

        if item == l[mid]:
            return True
        elif item > l[mid]:
            return binRecur(l, item, mid + 1, ri)
        elif item < l[mid]:
            return binRecur(l, item, li, mid - 1)
    else:
        return False


class HashList:
    def __init__(self, length):
        self.size = length
        self.slots = [None] * self.size

    def hashfunction(self, key):
        return key % self.size

    def rehash(self, oldhash):
        return (oldhash+1) % self.size

    def put(self, item):
        a = self.hashfunction(item)
        if self.slots[a] == None:
            self.slots[a] = item
        else:
            b = self.rehash(a)
            while self.slots[b] != None and a != b:
                b = self.rehash(b)
            if a == b:
                print("ERROR: List full")
            else:
                self.slots[b] = item

    def pl(self):
        print(self.slots)


for i in range(0, 11):
    print(binarysearch([1, 2, 3, 4, 5, 6, 7, 8, 9], i))
#a = HashList(9)
# a.put(9)
# a.put(20)
# a.put(7)
# a.put(91)
# a.put(16)
# a.put(8)
# a.pl()
