# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        que = deque()
        res = []
        que.append(root)

        while que:
            size = len(que)
            max = 1.0/float('inf')
            while size:
                node = que.popleft()
                if node.right:
                    que.append(node.right)
                if node.left:
                    que.append(node.left)
                if node.val > max:
                    max = node.val
                size -= 1
            
            res.append(max)
        return res
        