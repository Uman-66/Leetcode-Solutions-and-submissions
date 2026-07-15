class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        row_min = [min (matrix[i]) for i in range(m)]
        col_max = [max (matrix[i][j] for i in range(m)) for j in range (n)]
        
        ans = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == row_min[i] and matrix[i][j] == col_max[j]:
                    ans.append(matrix[i][j])
        
        return ans