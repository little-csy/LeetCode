# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node, parent, leng):
            if not node:
                return
            
            if node.val == parent+1:
                leng+=1
            else:
                leng = 1
            
            self.res = max(self.res, leng)

            dfs(node.left, node.val, leng)
            dfs(node.right, node.val, leng)
        
        dfs(root, root.val-1, 0)

        return self.res