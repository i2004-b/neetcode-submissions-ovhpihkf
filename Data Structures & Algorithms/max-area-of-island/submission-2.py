class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # DFS solution

        # Check if the graph exists
        if not grid:
            return 0

        # Get the rows and col
        ROWS, COLS = len(grid), len(grid[0])

        # Declare directions
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # Declare variable to track the max_area
        max_area = 0

        # Helper dfs function
        def dfs(r, c):
            # Base case: check bounds and if the location has been zeroed out
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0):
                return 0

            # Zero-out the location
            grid[r][c] = 0

            # Set count to 1
            count = 1

            # Iterate through direction and add to the count
            for dr, dc in directions:
                count += dfs(r + dr, c + dc)

            return count


        # Iterate through the graph
        for r in range(ROWS):
            for c in range(COLS):
                # Check if the current spot is "1"
                if grid[r][c] == 1:
                    # Run dfs on the current island and get count
                    area = dfs(r, c)
                    # Update max_area if needed
                    max_area = max(max_area, area)


        return max_area