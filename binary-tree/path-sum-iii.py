# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        que = deque()
        que.append(root)
        res = 0
        while que:
            size = len(que)
            while size:
                node = que.popleft()
                res += self.dfs(node, 0, targetSum)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                size -=1
        return res
    
    def dfs(self, root: Optional[TreeNode], num: int, targetSum: int) -> int:
        if root is None:
            return 0
        num += root.val
        cnt = 0
        if num == targetSum:
            cnt += 1
        cnt += self.dfs(root.left, num, targetSum)
        cnt += self.dfs(root.right, num, targetSum)
        return cnt