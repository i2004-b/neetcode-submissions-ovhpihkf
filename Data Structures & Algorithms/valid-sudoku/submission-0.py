class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # BRUTE FORCE SOLUTION
        # Rows and columns are set to 9
        ROWS, COLS = 9, 9

        # Iterate through the rows
        for i in range(ROWS):
            # Create hashmap for each value to be counted
            # count = {}
            # Can use a set because only getting one occurrence of each
            count = set()

            # Iterate through the columns (each item in the row)
            for j in range(COLS):
                # If blank spot, depicted by ".", go to next iteration
                if board[i][j] == ".":
                    continue
                # If the number is already seen, return false
                if board[i][j] in count:
                    return False
                count.add(board[i][j])

        # Iterate through the columns
        for i in range(COLS):
            # Set to hold the values when they show up
            count = set()
            
            # Iterate through each row
            for j in range(ROWS):
                # If the spot is empty, go on to the next iteration
                if board[j][i] == ".":
                    continue
                # If item already seen, return false
                if board[j][i] in count:
                    return False
                count.add(board[j][i])

        # Do the following for all 9 3x3 squares
        for square in range(9):
            # Make set for each square
            count = set()

            # Iterate through the rows
            for r in range(3):
                # Iterate through the columns
                for c in range(3):
                    # Figure out the row and column
                    row = (square // 3) * 3 + r
                    col = (square % 3) * 3 + c

                    if board[row][col] == ".":
                        continue
                    
                    if board[row][col] in count:
                        return False
                    
                    count.add(board[row][col])

        return True







