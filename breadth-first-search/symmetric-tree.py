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
        if left is None and right:
            return False
        elif right is None and left:
            return False
        elif right is None and left is None:
            return True
        elif right.val != left.val:
            return False
        else:
            outside = self.isSametree(left.left, right.right)
            inside = self.isSametree(left.right, right.left)
            if inside and outside:
                return True
            else:
                return False