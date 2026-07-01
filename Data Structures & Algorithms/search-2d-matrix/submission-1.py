class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Get the dimesnions of the matrix
        ROWS, COLS = len(matrix), len(matrix[0])

        """
        Conduct binary search in two parts:
        First --> find the row that the target may be in
        Second --> conduct a search on the finalized row
        """

        # First search is to find the right row
        top, bot = 0, ROWS - 1

        while top <= bot:
            # Find the middle row
            row = (top + bot) // 2

            # If the last number in the row is less than target, move the top row down
            if target > matrix[row][-1]:
                top = row + 1
            # If the first number in the row is greater than target, move the bottom row up
            elif target < matrix[row][0]:
                bot = row - 1
            # Else, you found the row that may contain the answer
            else:
                break

        # Check that you didn't break because a possible row did not exist
        if top > bot:
            return False

        # Declare pointers to the left and right to search through the row
        l, r = 0, COLS - 1
        
        while l <= r:
            # Calculate the middle index
            mid = (l + r) // 2

            # Check the value with the target
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True

        # If you exit out of the second loop, it means you could not find the value
        # Return False
        return False