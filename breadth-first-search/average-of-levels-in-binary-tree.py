# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []
        que = deque()
        res = []
        que.append(root)

        while que:
            size = len(que)
            num = size
            cnt = 0
            while size:
                node = que.popleft()
                cnt += node.val
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                size -= 1
            res.append(cnt/num)
        
        return res