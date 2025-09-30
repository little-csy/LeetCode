class Node:
    def __init__(self, key:int, value:int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.hash = {}
    
    def addn(self, node:Node):
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node

    def removen(self, node:Node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
    
    def get(self, key: int) -> int:
        if key in self.hash:
            node = self.hash[key]
            self.removen(node)
            self.addn(node)
            return node.value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            node = self.hash[key]
            self.removen(node)
        node = Node(key, value)
        self.hash[key] = node
        self.addn(node)

        if len(self.hash) > self.capacity:
            r = self.head.next
            self.removen(r)
            del self.hash[r.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)