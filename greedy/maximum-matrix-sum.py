class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        totals = 0
        n = len(matrix)
        minn = float('inf')
        neg = 0
        for i in range(n):
            for j in range(n):
                totals += abs(matrix[i][j])
                minn = min(minn, abs(matrix[i][j]))
                if matrix[i][j] <0:
                    neg+=1
        
        if neg%2 == 0:
            return totals
        else:
            return totals-2*minn

                