class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # Get rows and columns
        rows, cols = len(matrix), len(matrix[0])

        # Create 2-D array filled with zeros
        # Need to add 1 to the row and col for the zero padding 
        self.sums = [[0] * (cols + 1) for _ in range(rows + 1)]

        # Add sums to that point in the sums matrix
        for i in range(rows):
            # Keep track of row_sum
            row_sum = 0
            for j in range(cols):
                row_sum += matrix[i][j]
                # Add the row_sum + prev row's sum (from above)
                self.sums[i + 1][j + 1] = row_sum + self.sums[i][j + 1]

        


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Offset original coordinates by 1 to index into the sum array
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        # Take the total sum, at second coordinate
        total_sum = self.sums[row2][col2]
        # Take the upper sum
        upper = self.sums[row1 - 1][col2]
        # Take the left sum
        left = self.sums[row2][col1 - 1]
        # Value that was subtracted twice
        val = self.sums[row1 - 1][col1 - 1]

        return total_sum - upper - left + val


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)