# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def dfs(node):
            if not node:
                return ['#']
            res = []
            res.append(str(node.val))
            res += dfs(node.left)
            res += dfs(node.right)
            return res
        
        return ','.join(dfs(root))
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        val = data.split(',')
        self.index = 0

        def dfs():
            if val[self.index] == '#':
                self.index +=1
                return None
            node = TreeNode(int(val[self.index]))
            self.index +=1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))