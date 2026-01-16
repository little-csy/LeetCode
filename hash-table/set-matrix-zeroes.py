class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        seenr = set()
        seenc = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    seenr.add(i)
                    seenc.add(j)
        
        for val in seenr:
            for j in range(len(matrix[0])):
                matrix[val][j] = 0
        
        for val in seenc:
            for i in range(len(matrix)):
                matrix[i][val] = 0