class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
        self.pre = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.hp = {}
        self.capacity = capacity

    def addn(self, node):
        nxt = self.head.next
        self.head.next = node
        node.pre = self.head
        node.next = nxt
        nxt.pre = node
    
    def removen(self, node):
        nxt = node.next
        prev = node.pre
        prev.next = nxt
        nxt.pre = prev

    def get(self, key: int) -> int:
        if key in self.hp:
            node = self.hp[key]
            self.removen(node)
            self.addn(node)
            return node.value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.hp:
            node = self.hp[key]
            self.removen(node)
            del self.hp[key]
        newnode = Node(key, value)
        self.addn(newnode)
        self.hp[key] = newnode
        if len(self.hp)>self.capacity:
            last = self.tail.pre
            self.removen(last)
            del self.hp[last.key]
        

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)