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

            # grid[r][c] = "0"

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


"""
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
"""