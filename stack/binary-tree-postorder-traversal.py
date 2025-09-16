# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.postTrav(root)
        return self.res
    
    def postTrav(self, cur:Optional[TreeNode]):
        if cur is None:
            return
        
        self.postTrav(cur.left)
        self.postTrav(cur.right)
        self.res.append(cur.val)     