class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.pre = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.hash_map = {}
        self.capacity = capacity

    def addn(self, node: Node):
        p = self.head.next
        node.next = p
        p.pre = node
        self.head.next = node
        node.pre = self.head
    
    def removen(self, node: Node):
        nxt = node.next
        prv = node.pre
        prv.next = nxt
        nxt.pre = prv

    def get(self, key: int) -> int:
        if key in self.hash_map:
            p = self.hash_map[key]
            self.removen(p)
            self.addn(p)
            return p.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            p = self.hash_map[key]
            self.removen(p)
        n = Node(key,value)
        self.addn(n)
        self.hash_map[key] = n
        if len(self.hash_map)>self.capacity:
            t = self.tail.pre
            self.removen(t)
            del self.hash_map[t.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)