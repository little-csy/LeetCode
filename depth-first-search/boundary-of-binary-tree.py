# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root is None:
            return
        
        res.append(root.val)
        
        def isLeaf(node):
            if node and not node.left and not node.right:
                return True
            else:
                return False
        
        node = root.left
        while node:
            if not isLeaf(node):
                res.append(node.val)
            if node.left:
                node = node.left
            else:
                node = node.right
        
        def dfs(node):
            if not node:
                return
            if isLeaf(node):
                res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root.left)
        dfs(root.right)

        node = root.right
        stack = []
        while node:
            if not isLeaf(node):
                stack.append(node.val)
            if node.right:
                node = node.right
            else:
                node = node.left
        
        res.extend(stack[::-1])

        return res
            