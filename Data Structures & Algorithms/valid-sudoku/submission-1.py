class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # SINGLE PASS SOLUTION
        # Decalre hasmaps with the keys being the respective row, col, or square, and the value being a set
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set) # The key for each will be (r // 3, c // 3)

        # Iterate over the entire grid
        for r in range(9):
            for c in range(9):
                # If the value is blank go to next iteration
                if board[r][c] == ".":
                    continue

                # If the value already exists, return False
                if (board[r][c] in rows[r] 
                    or board[r][c] in cols[c] 
                    or board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                
                # Add the value to all respective areas
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        # Return True outside
        return True