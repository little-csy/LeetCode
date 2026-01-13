class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0
        
        front = {beginWord}
        back = {endWord}
        step = 1
        L = len(beginWord)

        while front and back:
            if len(front) > len(back):
                front, back = back, front
            
            nxt = set()
            
            for s in front:
                for i in range(L):
                    for v in "abcdefghijklmnopqrstuvwxyz":
                        news = s[:i] + v + s[i+1:]

                        if news in wordSet:
                            nxt.add(news)
                            wordSet.remove(news)
                        
                        if news in back:
                            return step+1
            front = nxt
            step += 1
        return 0