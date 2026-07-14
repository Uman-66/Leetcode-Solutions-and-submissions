class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        st_row, end_row, st_col, end_col = 0, m-1, 0, n-1
        ans = []
        while st_row<=end_row and st_col <= end_col:
            for j in range(st_col, end_col+1):
                ans.append(mat[st_row][j])
            for j in range(st_row+1, end_row+1):
                ans.append(mat[j][end_col])
            if st_row == end_row:
                break
            for j in range(end_col-1, st_col-1, -1):
                ans.append(mat[end_row][j])
            if st_col == end_col:
                break
            for j in range(end_row-1, st_row, -1):
                ans.append(mat[j][st_col])
            st_row+=1
            end_row-=1
            st_col+=1
            end_col-=1
        return ans