class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # Get rows and columns
        ROWS, COLS = len(matrix), len(matrix[0])
        # 2-D matrix with all 0s (extra row and column)
        self.prefix = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        # Iterate through putting the values into the prefix matrix
        for i in range(ROWS):
            row_sum = 0
            for j in range(COLS):
                # Add current value in the matrix to the row_sum
                row_sum += matrix[i][j]
                # Set the prefix item to be the row sum plus the value above
                self.prefix[i + 1][j + 1] = row_sum + self.prefix[i][j + 1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Add 1 to account for offset in prefix array
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        # Get total sum in the bottom corner
        total_sum = self.prefix[row2][col2]
        # Get sum of the upper row in the row above and in column2
        upper = self.prefix[row1 - 1][col2]
        # Get sum of the column to the left
        left = self.prefix[row2][col1 - 1]
        # Get value to add back before subtracted twice
        add = self.prefix[row1 - 1][col1 - 1]

        # Return the sum of the matrix region
        return total_sum - upper - left + add


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)