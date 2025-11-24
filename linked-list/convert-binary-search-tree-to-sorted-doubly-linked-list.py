"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        self.head = None
        self.prev = None

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)

            if self.prev is None:
                self.head = node
            else:
                self.prev.right = node
                node.left = self.prev
            
            self.prev = node

            dfs(node.right)
        
        dfs(root)

        self.head.left = self.prev
        self.prev.right = self.head

        return self.head