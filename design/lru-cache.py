class Node:
    def __init__(self, key:int, val:int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.mp = {}
        self.capacity = capacity

    def addn(self, node:Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    
    def removen(self, node:Node):
        p = node
        q = node.next
        q.prev = p.prev
        p.prev.next = q

    def get(self, key: int) -> int:
        if key in self.mp:
            p = self.mp[key]
            self.removen(p)
            self.addn(p)
            return p.val
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            p = self.mp[key]
            self.removen(p)
        node = Node(key, value)
        self.addn(node)
        self.mp[key] = node
        if len(self.mp) > self.capacity:
            n = self.tail.prev
            self.removen(n)
            del self.mp[n.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)