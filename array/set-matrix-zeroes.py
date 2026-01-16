class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        seen = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    seen.add(i)
                    seen.add(j)
        
        for val in seen:

            if val < len(matrix[0]):
                for i in range(len(matrix)):
                    matrix[i][val] = 0
            if val < len(matrix):
                for j in range(len(matrix[0])):
                    matrix[val][j] = 0