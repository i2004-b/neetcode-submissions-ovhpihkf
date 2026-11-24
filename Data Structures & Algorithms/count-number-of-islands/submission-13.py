class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0


        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        islands = 0
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if (r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visit or grid[r][c] == "0"):
                return 

            visit.add((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visit and grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1

        return islands
            