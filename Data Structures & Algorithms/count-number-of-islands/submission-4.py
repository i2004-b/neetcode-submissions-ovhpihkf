class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS without set --> zeroing out values

        # Check if the grid exists
        if not grid:
            return 0

        # Gets rows and cols
        ROWS, COLS = len(grid), len(grid[0])

        # Directions list
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # Islands tracker
        islands = 0

        def bfs(r, c):
            # Declare a queue
            queue = deque()

            # Add the initialy value to the queue
            queue.append((r, c))

            grid[r][c] = "0"

            # Iterate while the queue exists
            while queue:
                # Pop from the queue
                row, col = queue.popleft()

                # Zero out the value
                grid[row][col] = "0"

                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    # As long as these coordinates are valid, add to queue
                    if (0 <= r < ROWS and 0 <= c < COLS and grid[r][c] != "0"):
                        # Add to the queue
                        queue.append((r, c))
                        grid[r][c] = "0"


        # Iterate through the grid
        for r in range(ROWS):
            for c in range(COLS):
                # As long as the value is a 1, run bfs and increment islands
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1

        return islands