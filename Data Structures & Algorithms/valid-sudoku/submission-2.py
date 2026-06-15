class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = cols = 9

        # Track the numbers in the row
        for i in range(rows):
            track = set()
            for j in range(cols):
                if board[i][j] == ".":
                    continue
                if board[i][j] in track:
                    return False
                    
                track.add(board[i][j])

        
        # Track the numbers in the col
        for i in range(cols):
            track = set()
            for j in range(rows):
                if board[j][i] == ".":
                    continue
                
                if board[j][i] in track:
                    return False
                
                track.add(board[j][i])

        
        # Iterate over the 9 squares within the board
        for square in range(9):
            # Declare set to hold the values
            seen = set()
            # Iterate over the 3 rows and 3 columns in the square
            for r in range(3):
                for c in range(3):
                    # Calculate the correct row coordinate
                    row = (square // 3) * 3 + r
                    # Calculate the correct col coordinate
                    col = (square % 3) * 3 + c

                    # Rest is the same as before
                    if board[row][col] == ".":
                        continue

                    if board[row][col] in seen:
                        return False
                    
                    seen.add(board[row][col])


        return True
        

    