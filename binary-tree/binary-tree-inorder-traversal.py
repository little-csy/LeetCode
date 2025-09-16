# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.inTrav(root)
        return self.res
    

    def inTrav(self, cur:Optional[TreeNode]) -> None:
        if cur is None:
            return
        
        self.inTrav(cur.left)
        self.res.append(cur.val)
        self.inTrav(cur.right)