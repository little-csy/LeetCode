# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxval = float('-inf')
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        left = self.isValidBST(root.left)
        if root.val > self.maxval:
            self.maxval = root.val
        else:
            return False
        right = self.isValidBST(root.right)
        return right and left