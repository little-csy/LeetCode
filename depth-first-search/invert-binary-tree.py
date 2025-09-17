# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return 
        que = deque()
        que.append(root)

        while que:
            size = len(que)
            while size:
                node = que.popleft()
                node.right, node.left = node.left, node.right
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                size -= 1
        
        return root