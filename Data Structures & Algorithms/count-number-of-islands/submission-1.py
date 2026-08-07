class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS solution using set to track visited nodes

        # Identical beginning set up as dfs
        # Check if the grid exists
        if not grid:
            return 0

        # Get rows and cols
        ROWS, COLS = len(grid), len(grid[0])

        # Declare list with directions to go in
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # Declare set of visited items
        visit = set()

        # Declare variable to track islands
        islands = 0

        # Helper function
        def bfs(r, c): # Iterative
            # Want a queue to hold values
            queue = deque()

            # Add the first point to both the queue and the set
            queue.append((r, c))
            visit.add((r, c))

            # Iterate while the queue exists
            while queue:
                # Pop from the queue
                row, col = queue.popleft()

                # Want to add the new coordinates for the different directions
                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    # Check if the points are in bounds, check that they are "1", check that they haven't been visited
                    if (0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == "1" and (r, c) not in visit):
                        # Add to the queue and the set
                        queue.append((r, c))
                        visit.add((r, c))
            

        # Iterate through the grid
        for r in range(ROWS):
            for c in range(COLS):
                # Check if the current point is 1 and has not been visited
                if grid[r][c] == "1" and (r, c) not in visit:
                    # Run bfs
                    bfs(r, c)
                    # Update islands
                    islands += 1

        return islands
