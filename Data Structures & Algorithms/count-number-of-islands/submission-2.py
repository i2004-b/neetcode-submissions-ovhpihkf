class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS without using a set --> zeroing out locations
        # Check if grid exists
        if not grid:
            return 0

        # Get rows and cols
        ROWS, COLS = len(grid), len(grid[0])

        # Directions list
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # Variable to track islands
        islands = 0

        def dfs(r, c):
            # Check that it is a valid location: check bounds and that it is 1
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0"):
                return

            # Zero out the location
            grid[r][c] = "0"

            # DFS in each direction
            for dr, dc in directions:
                dfs(r + dr, c + dc)


        for r in range(ROWS):
            for c in range(COLS):
                # Just check that the grid is 1
                if grid[r][c] == "1":
                    # Run dfs
                    dfs(r, c)
                    # Increment islands
                    islands += 1


        return islands