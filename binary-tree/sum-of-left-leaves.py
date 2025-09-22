# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.right is None and root.left is None:
            return 0
        left = self.sumOfLeftLeaves(root.left)
        if root.left and root.left.right is None and root.left.left is None:
            left += root.left.val
        right = self.sumOfLeftLeaves(root.right)
        sum = left+right
        return sum 