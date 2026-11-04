class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
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
