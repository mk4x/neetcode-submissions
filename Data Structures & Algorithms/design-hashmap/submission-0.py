class ListNode:
    def __init__(self, key=-1, val=-1, nxt = None):
        self.key = key
        self.val = val
        self.nxt = nxt

class MyHashMap:

    def __init__(self):
        self.mp = [ListNode() for _ in range(1000)]
        
    def hash(self, key):
        return key % len(self.mp)

    def put(self, key: int, value: int) -> None:
        cur = self.mp[self.hash(key)]
        while cur.nxt: 
            if cur.nxt.key == key:
                cur.nxt.val = value
                return
            cur = cur.nxt
        cur.nxt = ListNode(key, value)

    def get(self, key: int) -> int:
        cur = self.mp[self.hash(key)]
        while cur.nxt:
            if cur.nxt.key == key:
                return cur.nxt.val
            cur = cur.nxt
        return -1

    def remove(self, key: int) -> None:
        cur = self.mp[self.hash(key)]
        while cur.nxt:
            if cur.nxt.key == key:
                cur.nxt = cur.nxt.nxt
                return
            cur = cur.nxt


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)