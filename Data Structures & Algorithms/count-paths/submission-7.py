class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # More clear 2-D Solution
        grid = [1] * n

        for _ in range(m - 1):
            new_row = [1] * n
            for j in range(n - 2, -1, -1):
                new_row[j] = grid[j] + new_row[j + 1]

            grid = new_row

        return grid[0]