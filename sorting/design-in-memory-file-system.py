class Node:
    def __init__(self):
        self.child = {}
        self.isFile = False
        self.content = ""

class FileSystem:

    def __init__(self):
        self.root = Node()
        
    def ls(self, path: str) -> List[str]:
        cur = self.root
        if path!='/':
            for part in path.split('/')[1:]:
                cur = cur.child[part]
        if cur.isFile:
            return [path.split('/')[-1]]
        else:
            return sorted(cur.child.keys())
    
    def mkdir(self, path: str) -> None:
        cur = self.root
        for part in path.split('/')[1:]:
            if part not in cur.child:
                cur.child[part] = Node()
            cur = cur.child[part]
        
    def addContentToFile(self, filePath: str, content: str) -> None:
        cur = self.root
        for part in filePath.split('/')[1:]:
            if part not in cur.child:
                cur.child[part] = Node()
            cur = cur.child[part]
        cur.isFile = True
        cur.content += content
        
    def readContentFromFile(self, filePath: str) -> str:
        cur = self.root
        for part in filePath.split('/')[1:]:
            cur = cur.child[part]
        return cur.content

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)