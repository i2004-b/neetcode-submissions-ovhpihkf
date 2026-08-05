class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        dp = [1, 2]

        for _ in range(2, n):
            # tmp = dp[1]
            # dp[1] = dp[0] + dp[1]
            # dp[0] = tmp
            dp[0], dp[1] = dp[1], dp[0] + dp[1]

        return dp[1]