class Solution:
    def searchrow(self, matrix: List[List[int]], target: int, row: int) -> bool:
        n = len(matrix[0])
        st = 0
        end = n-1
        while(st<=end):
            mid = st + (end-st)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                end = mid-1
            else:
                st = mid+1
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n  = len(matrix[0])

        st_row = 0
        end_row = m-1
        while(st_row<=end_row):
            mid = st_row + (end_row-st_row)//2

            if target >= matrix[mid][0] and target <= matrix[mid][n-1]:
                return self.searchrow(matrix, target, mid)
            elif target > matrix[mid] [n-1]:
                st_row = mid + 1
            else:
                end_row = mid - 1
        return False