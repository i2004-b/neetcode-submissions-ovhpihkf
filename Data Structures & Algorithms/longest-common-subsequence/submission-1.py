class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        # Declare cache to work with
        dp = [[-1] * m for _ in range(n)]

        def memoization(i, j):
            # Check if in bounds
            if i == n or j == m:
                return 0
            
            # Check if value accounted for in dp
            if dp[i][j] != -1:
                return dp[i][j]

            # Check if the letters are equal
            if text1[i] == text2[j]:
                dp[i][j] = 1 + memoization(i + 1, j + 1)
            else:
                dp[i][j] = max(memoization(i + 1, j), memoization(i, j + 1))

            return dp[i][j]

        memoization(0, 0)
        return dp[0][0]