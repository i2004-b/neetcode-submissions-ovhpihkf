class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create 2-D grid
        grid = [1] * n
        prev = [0] * n
        prev[-1] = 1

        for i in range(m - 1):
            # Iterate backwards in grid
            for j in range(n - 2, -1, -1):
                prev[j] = grid[j] + prev[j + 1]
            # Set grid to prev
            grid = prev

        return grid[0]