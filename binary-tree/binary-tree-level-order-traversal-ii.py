# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        que = deque()
        res = []
        que.append(root)

        while que:
            size = len(que)
            vec = []
            while size:
                node = que.popleft()
                vec.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)  
                size -= 1
            
            res.append(vec)
        
        return res[::-1]