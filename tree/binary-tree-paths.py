# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        path = []
        self.backtracking(root, path, res)
        return res
    
    def backtracking(self, root:Optional[TreeNode], path:List[int], res:List[str]):
        if root:
            path.append(root.val)

        if root.left is None and root.right is None:
            res.append('->'.join(map(str,path)))
            return
        
        if root.left:
            self.backtracking(root.left, path, res)
            path.pop()
        
        if root.right:
            self.backtracking(root.right, path, res)
            path.pop()