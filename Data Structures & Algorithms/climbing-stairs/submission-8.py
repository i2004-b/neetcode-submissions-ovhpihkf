class Solution:
    def climbStairs(self, n: int) -> int:
        """
        cache = {}
        cache[n] = 1
        def rec(step):
            if step > n:
                return 0
            if step in cache:
                return cache[step]

            cache[step] = 0
            cache[step] += rec(step + 1)
            cache[step] += rec(step + 2)

            return cache[step]

        rec(0)
        return cache[0]
        """

        """
        steps = [0] * (n + 1)
        steps[-1] = 1

        for i in range(len(steps) - 2, -1, -1):
            steps[i] = steps[i + 1] + (steps[i + 2] if i + 2 < len(steps) else 0)

        return steps[0]
        """

        dp1, dp2 = 1, 1

        for i in range(n - 1):
            dp1, dp2 = dp1 + dp2, dp1

        return dp1


