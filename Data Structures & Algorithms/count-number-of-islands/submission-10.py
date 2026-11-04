class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        count = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])

        def BFS(r, c):
            # Push the starting cell into the queue
            queue = deque()
            queue.append((r, c))

            # Zero out initial cell
            grid[r][c] = "0"

            # Iterate while queue is non-empty
            while queue:
                # Pop from the queue
                r, c = queue.popleft()

                for d in directions:
                    dr, dc = r + d[0], c + d[1]

                    if 0 <= dr < ROWS and 0 <= dc < COLS and grid[dr][dc] == "1":
                        grid[dr][dc] = "0"
                        queue.append((dr, dc))
        

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    # Run bfs from location
                    BFS(r, c)
                    count += 1

        return count
