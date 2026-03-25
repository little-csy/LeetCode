class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        w1 = -1
        w2 = -1
        minl = float('inf')

        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                w1 = i
                if w2 != -1:
                    minl = min(minl, abs(w2-w1))
            
            if wordsDict[i] == word2:
                w2 = i
                if w1 != -1:
                    minl = min(minl, abs(w2-w1))
        
        return minl