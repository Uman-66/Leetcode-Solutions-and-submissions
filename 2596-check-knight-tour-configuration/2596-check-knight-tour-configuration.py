class Solution:
    def isvalid(self, grid, r, c, n, expval):
        if r<0 or c<0 or r>=n or c>=n or grid[r][c]!=expval:
            return False
        if expval == n*n-1:
            return True
        ans1 = self.isvalid( grid, r-2, c+1, len(grid),expval+1 )
        ans2 = self.isvalid(grid, r-1, c+2, len(grid),expval+1 )
        ans3 = self.isvalid(grid, r+1, c+2, len(grid),expval+1 )
        ans4 = self.isvalid(grid, r+2, c+1, len(grid),expval+1 )
        ans5 = self.isvalid(grid, r+2, c-1, len(grid),expval+1 )
        ans6 = self.isvalid(grid, r+1, c-2, len(grid),expval+1 )
        ans7 = self.isvalid(grid, r-1, c-2, len(grid),expval+1 )
        ans8 = self.isvalid(grid, r-2, c-1, len(grid),expval+1 )
        return ans1 or ans2 or ans3 or ans4 or ans5 or ans6 or ans7 or ans8
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        return self.isvalid(grid, 0, 0, len(grid), 0)