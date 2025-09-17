"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        que = deque()
        res = []
        que.append(root)

        while que:
            size = len(que)
            vec = []
            while size:
                node = que.popleft()
                vec.append(node.val)
                for child in node.children:
                    que.append(child)
                size -=1
            
            res.append(vec)
        
        return res


        