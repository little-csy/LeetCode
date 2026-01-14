# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return
        if p == root or q == root:
            return root
        
        self.lowestCommonAncestor(root.left, p, q)
        self.lowestCommonAncestor(root.right, p, q)
        if root.left and root.right:
            return root
        if not root.left and root.right:
            return root.right
        if not root.right and root.left:
            return root.left