"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return
        que = deque()
        que.append(root)
        while que:
            size = len(que)
            pre = None
            while size:
                node = que.popleft()
                if pre:
                    pre.next = node
                pre = node
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                size -= 1
            pre.next = None
        return root 