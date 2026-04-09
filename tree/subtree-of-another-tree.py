# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        def isSame(t1,t2):
            if not t1 and not t2:
                return True
            elif not t1 or not t2:
                return False
            elif t1.val != t2.val:
                return False
            left = isSame(t1.left,t2.left)
            right = isSame(t1.right,t2.right)
            return left and right
        
        if isSame(root, subRoot):
            return True
        
        cmpl = self.isSubtree(root.left,subRoot)
        cmpr = self.isSubtree(root.right,subRoot)
        return cmpl or cmpr