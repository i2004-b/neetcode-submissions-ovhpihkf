class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS with set solution
        # Time: O(m * n), Space: O(m * n)

        # If the grid does not exist, return 0
        if not grid:
            return 0

        # Get the rows and columns
        ROWS, COLS = len(grid), len(grid[0])

        # Define directions to go in
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # Declare count variable and set
        count = 0
        seen = set()

        # Run dfs
        def dfs(r, c):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in seen or grid[r][c] == "0"):
                return

            seen.add((r, c))

            for d in directions:
                dfs(r + d[0], c + d[1])

            return

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in seen:
                    dfs(r, c)
                    count += 1

        return count
                
        
        """
        self.count = 0
        seen = set()

        def dfs(r, c, island):
            if (r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or
                (r, c) in seen or grid[r][c] == "0"):
                return
            
            seen.add((r, c))

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for d in directions:
                dfs(r + d[0], c + d[1], False)

            if island:
                self.count += 1

            return

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                dfs(r, c, True)

        return self.count
        """
