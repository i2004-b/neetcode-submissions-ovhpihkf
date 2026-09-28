class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Set a left and right pointer (leftmost and rightmost column)
        left, right = 0, len(matrix) - 1

        # Iterate while l < r (if equal, just a single element and there is nothing to do)
        while left < right:
            # Have a top and bottom pointer
            # Top points to the first row; bottom points to the last row
            top, bottom = left, right

            # Iterate one less than the side length (r - l)
            for i in range(right - left):
                # Save the top, leftmost value
                t_leftmost = matrix[top][left + i]

                # Start swapping backwards
                matrix[top][left + i] = matrix[bottom - i][left]
                matrix[bottom - i][left] = matrix[bottom][right - i]
                matrix[bottom][right - i] = matrix[top + i][right]
                matrix[top + i][right] = t_leftmost

            left += 1
            right -= 1

        

                