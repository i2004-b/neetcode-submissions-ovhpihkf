class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left, right = 0, len(matrix) - 1

        # Iterate as long as right and left do not equal or surpass each other
        while left < right:
            # Declare a top and bottom pointer (point to top and bottom rows)
            top, bottom = left, right

            # Iterate n - 1 times, where n - 1 equals r - l
            for i in range(right - left):
                # Save the top leftmost item
                t_leftmost = matrix[top][left + i]

                # Swap items
                matrix[top][left + i] = matrix[bottom - i][left]
                matrix[bottom - i][left] = matrix[bottom][right - i]
                matrix[bottom][right - i] = matrix[top + i][right]
                matrix[top + i][right] = t_leftmost
            
            # Increment left and decrement right
            left += 1
            right -= 1