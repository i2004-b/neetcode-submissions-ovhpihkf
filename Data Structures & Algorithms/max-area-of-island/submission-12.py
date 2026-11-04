class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        max_area = 0

        def dfs(r, c):
            # Zero out the point
            grid[r][c] = 0
            # Add to the stack
            stack = []
            stack.append((r, c))
            area = 1

            # Iterate while the stack exists
            while stack:
                r, c = stack.pop()

                # Add points from all four directions
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1):
                        area += 1
                        grid[nr][nc] = 0
                        stack.append((nr, nc))

            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    count = dfs(r, c)
                    max_area = max(max_area, count)

        return max_area








        
        
        
        
        """
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            # Check that the point is in bounds and is a 1
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 00):
                return 0

            # Zero out current location
            grid[r][c] = 0
            size = 1

            # Add to the size through the directions
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                size += dfs(nr, nc)
            
            return size


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    count = dfs(r, c)
                    max_area = max(max_area, count)

        return max_area
        """
