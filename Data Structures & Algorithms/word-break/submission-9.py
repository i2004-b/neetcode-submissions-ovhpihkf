class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        cache = {}
        cache[len(s)] = True

        def dfs(i):
            if i in cache:
                return cache[i]

            cache[i] = False
            for word in wordDict:
                n = len(word)
                if s[i : i + n] == word and dfs(i + n):
                    cache[i] = True
                    return cache[i]

            return cache[i]

        return dfs(0)
        """

        dp = [False] * (len(s) + 1)
        dp[-1] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                n = len(word)
                if s[i : i + n] == word:
                    dp[i] |= dp[i + n]
                    

        return dp[0]

        



                        