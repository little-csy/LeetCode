# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left = root.left
        right = root.right
        leftnum = 0
        rightnum = 0
        while left:
            left = left.left
            leftnum += 1
        while right:
            right = right.right
            rightnum += 1
        if leftnum == rightnum:
            return 2 ** (leftnum+1) - 1
        left = self.countNodes(root.left)
        right = self.countNodes(root.right)
        return left+right+1
