# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.output = []
        self.inorder(root)
        return self.output
    
    def inorder(self, root: Optional[TreeNode]):
        if root is None:
            return
        self.inorder(root.left)
        self.output.append(root.val)
        self.inorder(root.right)
    