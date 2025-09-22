# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        if (self.Trav(root, targetSum-root.val)):
            return True
        else:
            return False
        
    def Trav(self, root: Optional[TreeNode], target: int) -> bool:
        if root.right is None and root.left is None:
            if target == 0:
                return True
            else:
                return False
        
        if root.left:
            target -= root.left.val
            if(self.Trav(root.left, target)):
                return True
            target += root.left.val
        
        if root.right:
            target -= root.right.val
            if (self.Trav(root.right, target)):
                return True
            target += root.right.val
        
        return False