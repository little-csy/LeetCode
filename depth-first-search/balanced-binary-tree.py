# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = self.height(root)
        if res == -1:
            return False
        else:
            return True
    
    def height(self, node:Optional[TreeNode]) -> int:
        if node is None:
            return 0
        left = self.height(node.left)
        if left == -1:
            return -1
        right = self.height(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        else:
            return 1+max(left, right)