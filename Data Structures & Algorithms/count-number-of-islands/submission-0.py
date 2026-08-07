class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS Solution using a set to track visited nodes
        
        # Check if the grid exists
        if not grid:
            return 0

        # Get rows and columns of grid
        rows, cols = len(grid), len(grid[0])

        # Declare directions for dfs to go in
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # Declare set to keep track of visited nodes
        visit = set()

        # Variable to keep track of islands
        islands = 0

        # Helper dfs function that takes as input r and c
        def dfs(r, c):
            # Base case: check if in bounds, if the value is 0, if the value has already been visited
            if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0" or (r, c) in visit):
                return

            # Add the point to visit
            visit.add((r, c))

            # Run dfs in each direction
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # Iterate through the points in the graph
        for r in range(rows):
            for c in range(cols):
                # Check that the value is 1 and it has not been visited
                if grid[r][c] == "1" and (r, c) not in visit:
                    # Run dfs
                    dfs(r, c)
                    # Increment islands
                    islands += 1

        return islands