# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = []
        self.dfs(root)
        return self.res[k-1]
    
    def dfs(self, root: Optional[TreeNode]):
        if root is None:
            return
        if root.left:
            self.dfs(root.left)
        self.res.append(root.val)
        if root.right:
            self.dfs(root.right)

        