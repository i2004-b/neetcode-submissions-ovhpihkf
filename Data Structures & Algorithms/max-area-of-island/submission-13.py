class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # BFS
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        max_area = 0

        def bfs(r, c):
            queue = deque()
            # Add point to the queue
            queue.append((r, c))
            # Zero out the point
            grid[r][c] = 0
            area = 1

            # Iterate while the queue is non-empty
            while queue:
                # Pop from the queue
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1):
                        queue.append((nr, nc))
                        grid[nr][nc] = 0
                        area += 1

            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    count = bfs(r, c)
                    max_area = max(max_area, count)

        return max_area