class Solution:
    def transpose(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        ans = [[0] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                ans[j][i] = mat[i][j]
        return ans