class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Check if grid exists
        if not grid:
            return 0

        # Get rows and columns
        ROWS, COLS = len(grid), len(grid[0])

        # Declare directions
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        # Set the max area
        max_area = 0

        # Helper bfs function
        def bfs(r, c):
            # Declare queue and add point to it
            queue = deque([(r, c)])

            # Zero-out the location
            grid[r][c] = 0

            # Set count to 1
            count = 1

            # Iterate while the queue exists
            while queue:
                # Pop from the queue
                row, col = queue.popleft()

                # Check each direction and add to the queue
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    
                    # Check if the points are in bounds and not 0
                    if (0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == 1):
                        # Add to the queue
                        queue.append((r, c))
                        # Zero-out the location
                        grid[r][c] = 0
                        count += 1

            return count


        # Iterate through the grid
        for r in range(ROWS):
            for c in range(COLS):
                # Run bfs if the location is 1
                if grid[r][c] == 1:
                    max_area = max(max_area, bfs(r, c))

        return max_area