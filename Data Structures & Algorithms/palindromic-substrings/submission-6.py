class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        res = 0

        dp = [[False] * length for _ in range(length)]

        for i in range(length - 1, -1, -1):
            for j in range(i, length):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    res += 1


        return res