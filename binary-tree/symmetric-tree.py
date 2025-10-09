# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSametree(root.left, root.right)
    
    def isSametree(self, left:Optional[TreeNode], right:Optional[TreeNode]) -> bool:
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False
        elif left.val != right.val:
            return False
        outside = self.isSametree(left.left, right.right)
        inside = self.isSametree(left.right, right.left)
        return outside and inside