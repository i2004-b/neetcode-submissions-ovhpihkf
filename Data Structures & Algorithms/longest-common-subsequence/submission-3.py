class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        dp = [0] * (n + 1)

        for i in range(m):
            cache = [0] * (n + 1)
            for j in range(n):
                if text1[i] == text2[j]:
                    cache[j + 1] = 1 + dp[j]
                else:
                    cache[j + 1] = max(cache[j], dp[j + 1])

            dp = cache

        return dp[-1]
                