class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix[0]) - 1

        for row, column_num in enumerate(matrix):
            if matrix[row][left] <= target <= matrix[row][right]:
                while left <= right:
                    mid = (left + right) // 2

                    if target > matrix[row][mid]:
                        left = mid + 1
                    elif target < matrix[row][mid]:
                        right = mid - 1
                    else:
                        return True
            
        return False