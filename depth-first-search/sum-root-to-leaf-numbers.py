# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        self.dfs(root, 0)
        return self.sum
    
    def dfs(self, root: Optional[TreeNode], num: int) -> int:
        num = num*10 + root.val
        if root.right is None and root.left is None:
            self.sum += num
            return
        
        if root.right:
            self.dfs(root.right, num)
        if root.left:
            self.dfs(root.left, num)