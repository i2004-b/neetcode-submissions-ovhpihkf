class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        One pass solution for binary search:
            treating the whole matrix as one long, flat array
        """

        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS * COLS - 1

        while l <= r:
            # Find the middle value
            mid = (l + r) // 2

            # Find the row and column holding the middle value
            row = mid // COLS
            col = mid % COLS

            # Check the values
            if target > matrix[row][col]:
                l = mid + 1
            elif target < matrix[row][col]:
                r = mid - 1
            else:
                return True

        return False