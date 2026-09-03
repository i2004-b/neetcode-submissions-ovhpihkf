class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 1-D Solution

        # Declare an array filled with ones
        row = [1] * n

        # Iterate m - 1 times
        for _ in range(m - 1):
            # Iterate through elements from the second to last onward
            for j in range(n - 2, -1, -1):
                row[j] += row[j + 1]

        return row[0]