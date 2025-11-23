# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(node, s):
            if not node:
                return
            
            s+=node.val
            path.append(node.val)

            if not node.left and not node.right:
                if s==targetSum:
                    res.append(path[:])
            
            dfs(node.left,s)
            dfs(node.right,s)
            path.pop()
        
        dfs(root,0)
        return res
        