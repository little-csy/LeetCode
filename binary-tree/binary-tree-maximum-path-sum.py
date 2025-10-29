# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxsum = float('-inf')
        self.dfs(root)
        return self.maxsum
    
    def dfs(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        left = 0 if left<0 else left
        right = 0 if right<0 else right
        self.maxsum = max(left+right+root.val, self.maxsum)
        return max(left+root.val, right+root.val)
        

        