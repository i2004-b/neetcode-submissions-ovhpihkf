class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Get lengths of text1 and text2
        n, m = len(text1), len(text2)
        
        
        # Declare DP array with extra column of 0s
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # i goes with n (for i in range(n))
        # j goes with m (for j in range(m))
        for i in range(n):
            for j in range(m):
                # Check if they are equal
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = 1 + dp[i][j]
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[n][m]
