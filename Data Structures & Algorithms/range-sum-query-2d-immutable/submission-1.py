class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # Get rows and columns
        ROWS, COLS = len(matrix), len(matrix[0])
        # Create matrix with extra row and column
        self.prefix = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        # Iterate through the rows
        for i in range(1, ROWS + 1):
            # Track the sum for each row
            row_sum = 0
            # Iterate through the columns
            for j in range(1, COLS + 1):
                row_sum += matrix[i - 1][j - 1]
                self.prefix[i][j] = row_sum + self.prefix[i - 1][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Account for offset array
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        # Total is at the second coordinate
        total = self.prefix[row2][col2]
        # Above prefix sum is the row above the first but same column as the last
        above = self.prefix[row1 - 1][col2]
        # Left prefix sum is the same row as the last coordinate by the column before the first
        left = self.prefix[row2][col1 - 1]
        # Value at the top left corner taken away twice, so add it back
        # Row before the first row and the column before the first column
        add = self.prefix[row1 - 1][col1 - 1]

        # Return the total - above - left + add
        return total - above - left + add


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)