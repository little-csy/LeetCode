from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordlistset = set(wordList)
        if endWord not in wordlistset:
            return 0
        visit = set()
        visit.add(beginWord)
        q= deque()
        q.append((beginWord,1))

        while q:
            word, step = q.popleft()

            if word == endWord:
                return step

            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newword = word[:i] + c + word[i+1:]
                    if newword in wordlistset and newword not in visit:
                        visit.add(newword)
                        q.append((newword,step+1)) 

        return 0                      