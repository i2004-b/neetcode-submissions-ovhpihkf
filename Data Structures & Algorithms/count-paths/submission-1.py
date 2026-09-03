class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Recursive solution with memoization

        # Declare 2-d grid to store paths from that location
        grid = [[-1 for _ in range(n)] for _ in range(m)]

        # Set destination as 0
        grid[m-1][n-1] = 1

        def dfs(x, y):
            if x == m or y == n:
                return 0
            if x == m - 1 and y == n - 1:
                return 1
            if grid[x][y] > -1:
                return grid[x][y]

            res = 0
            res += dfs(x + 1, y)
            res += dfs(x, y + 1)

            grid[x][y] = res

            return res

        return dfs(0, 0)