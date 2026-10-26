class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Pure brute force recursion:
        Idea: pass in the amount into the dfs
        Base Cases: if 0, return 0; if less than 0, return 1e9
        Set result to initially be 1e9
        Iterate over the coins in the array and set res = min(dfs(i - coin) + 1, 1e9)
        return res

        After you call dfs, if it returns 1e9, return -1, else return the number

        def dfs(total):
            if total == 0:
                return 0
            elif total < 0:
                return 1e9

            res = 1e9

            for c in coins:
                res = min(1 + dfs(total - c), res)

            return res

        ans = dfs(amount)

        return -1 if ans >= 1e9 else ans
        """

        cache = {0: 0}

        def dfs(total):
            if total in cache:
                return cache[total]
            elif total < 0:
                return 1e9

            res = 1e9

            for c in coins:
                res = min(1 + dfs(total - c), res)
            
            cache[total] = res

            return res

        ans = dfs(amount)

        return -1 if ans >= 1e9 else ans

        