# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        que = deque()
        que.append(root)
        res = []

        while que:
            size = len(que)
            first = size

            while size:
                node = que.popleft()
                if first == size:
                    res.append(node.val)
                if node.right:
                    que.append(node.right)
                if node.left:
                    que.append(node.left)
                size -= 1
        
        return res
                