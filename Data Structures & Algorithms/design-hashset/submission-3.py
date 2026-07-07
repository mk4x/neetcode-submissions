from random import randint


class Node:
    def __init__(self, data, nxt=None, prev=None):
        self.data = data
        self.nxt = nxt
        self.prev = prev

    def remove_self(self):
        if self.prev is not None:
            self.prev.nxt = self.nxt
        if self.nxt is not None:
            self.nxt.prev = self.prev

    def add_next(self, data):
        self.nxt = Node(data, None, self)


class LinkedList:
    def __init__(self, head=None):
        self.head = head


class HashUtil:
    def __init__(self, l=50, r=500):
        self.M = self.get_random_prime(l, r)

    def fermat(self, n, k=10):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0:
            return False
        for _ in range(k):
            a = randint(2, n - 2)
            if pow(a, n - 1, n) != 1:
                return False
        return True

    def get_random_prime(self, l, r):
        prime = randint(l, r)
        while not self.fermat(prime):
            prime = randint(l, r)        
        return prime

    def calc(self, k):
        return k % self.M


class MyHashSet:
    def __init__(self):
        self.calcer = HashUtil()
        self.table = [None for _ in range(self.calcer.M)]   # range(), and no mapper

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        location = self.calcer.calc(key)
        LL = self.table[location]
        if LL is None or LL.head is None:         
            self.table[location] = LinkedList(Node(key))
        else:
            node = LL.head
            while node.nxt is not None:
                node = node.nxt
            node.add_next(key)

    def remove(self, key: int) -> None:
        location = self.calcer.calc(key)
        LL = self.table[location]
        if LL is None:
            return
        node = LL.head
        while node is not None:
            if node.data == key:
                if node.prev is None:              # head
                    LL.head = node.nxt
                    if node.nxt is not None:
                        node.nxt.prev = None
                    else:
                        self.table[location] = None  
                else:
                    node.remove_self()
                return
            node = node.nxt

    def contains(self, key: int) -> bool:
        location = self.calcer.calc(key)
        LL = self.table[location]
        if LL is None or LL.head is None:
            return False
        node = LL.head
        while node is not None:                 
            if node.data == key:                
                return True
            node = node.nxt
        return False