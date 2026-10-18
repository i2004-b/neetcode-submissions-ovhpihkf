class Solution:
    def climbStairs(self, n: int) -> int:
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
