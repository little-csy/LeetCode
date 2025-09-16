# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.preTrav(root, self.res)
        return self.res

    def preTrav(self, cur:Optional[TreeNode], res:List[int]) -> None:
        if cur is None:
            return
        self.res.append(cur.val)
        self.preTrav(cur.left, self.res)
        self.preTrav(cur.right, self.res)
