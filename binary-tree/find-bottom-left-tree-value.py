# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        res = 0
        que = deque()
        que.append(root)
        while que:
            size = len(que)
            first = len(que)
            while size:
                node = que.popleft()
                if size == first:
                    res = node.val
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                size -= 1
        return res

        