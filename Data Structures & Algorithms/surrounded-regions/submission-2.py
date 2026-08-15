class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Get the rows and columns of the board
        ROWS, COLS = len(board), len(board[0])

        # Create dfs function to turn "O"s into "T"s
        def dfs(r, c):
            # Check if in bounds and that the location is an "O"
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O":
                return

            # Turn the location into T
            board[r][c] = "T"

            # Run dfs in four directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # First phase: check the border items and if any of them are Os, turn them into Ts
        for r in range(ROWS):
            for c in range(COLS):
                # Check if the item is "O" and that it is on the border
                if board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1]):
                    # Run dfs
                    dfs(r, c)

        # Second phase: turn the remaining Os into Ts
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # Third phase: turn the Ts into Os
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"

            