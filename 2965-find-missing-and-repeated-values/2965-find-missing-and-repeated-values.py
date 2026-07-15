class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        actsum = 0
        seen = set()
        ans = []
        for i in range(len(grid)):
            for j in range(n):
                num = grid[i][j]
                actsum+=grid[i][j]
                if num in seen:
                    ans.append(num)
                seen.add(num)
        expnum = n*n*(n*n+1)//2
        b = expnum -actsum+ans[0]
        ans.append(b)
        return ans