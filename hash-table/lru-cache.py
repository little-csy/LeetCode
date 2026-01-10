class Node:
    def __init__(self, key:int, value:int):
        self.key = key
        self.value= value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.mp = {}
        
    def addn(self, node:Node):
        nxt = self.head.next
        nxt.prev = node
        self.head.next = node
        node.prev = self.head
        node.next = nxt
    
    def removen(self, node:Node):
        pre = node.prev
        nxt = node.next
        pre.next = nxt
        nxt.prev = pre

    def get(self, key: int) -> int:
        if key in self.mp:
            node = self.mp[key]
            self.removen(node)
            self.addn(node)
            return node.value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            node = self.mp[key]
            node.value = value
            self.removen(node)
            self.addn(node)
        else:
            if len(self.mp) >= self.capacity:
                last = self.tail.prev
                self.removen(last)
                del self.mp[last.key]
            node = Node(key, value)
            self.addn(node)
            self.mp[key] = node

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)