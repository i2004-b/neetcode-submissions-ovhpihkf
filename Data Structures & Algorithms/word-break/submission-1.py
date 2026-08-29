class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1) # +1 to account for the base case (if you get to the end: True)
        # Set base case
        dp[-1] = True

        # Iterate backwards through the string
        for i in range(len(s) - 1, -1, -1):
            # Iterate through every word in the list of words
            for w in wordDict:
                # Check if the length will work and if the words are equal
                if (i + len(w) <= len(s)) and s[i : i + len(w)] == w:
                    # Set dp to whether or not when that word is used the end can be used as well
                    dp[i] = dp[i + len(w)]

                if dp[i]:
                    break

        return dp[0]