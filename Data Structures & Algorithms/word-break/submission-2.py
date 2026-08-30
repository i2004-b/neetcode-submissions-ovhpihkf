class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Set array to false initially
        dp = [False] * (len(s) + 1)
        # Set base case
        dp[-1] = True

        # Iterate backwards through the string
        for i in range(len(s) - 1, -1, -1):
            # Iterate through words in wordDict
            for w in wordDict:
                # Check length and if the word is equal
                if (i + len(w) <= len(s)) and s[i: i + len(w)] == w:
                    dp[i] = dp[i + len(w)]

                if dp[i] == True:
                    break

        return dp[0]