# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        que = deque()
        que.append(root)
        cnt = 1

        while que:
            size = len(que)
            while size:
                node = que.popleft()
                if not node.right and not node.left:
                    return cnt
                if node.right:
                    que.append(node.right)
                if node.left:
                    que.append(node.left)
                size -=1
            cnt += 1