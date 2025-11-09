class TrieNode:
    def __init__(self):
        self.child = {}
        self.isend = False
class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node.child:
                node.child[w] = TrieNode()
            node = node.child[w]
        node.isend = True
        
    def search(self, word: str) -> bool:
        node = self.root
        for w in word:
            if w not in node.child:
                return False
            node = node.child[w]
        return node.isend
        
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for w in prefix:
            if w not in node.child:
                return False
            node = node.child[w]
        return True
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)