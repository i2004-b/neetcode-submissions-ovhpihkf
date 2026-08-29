class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # DP Bottom Up Solution
        # Idea: if you have a word until a certain point, can the rest of the string be a valid word?
        # Time: O(n * m * t) where n is the length of the string, m is the number of words, and t is the length of word
        # Space: O(n) where n is the length of the string

        # Declare an array to hold whether or not a word can be formed from there
        # Have an extra slot as the base case: getting to the end of the list is considered True
        dp = [False] * (len(s) + 1)
        # Set base case
        dp[-1] = True

        # Iterate backwards through the string
        for i in range(len(s) - 1, -1, -1):
            # Iterate for every single word
            for w in wordDict:
                # To set value, check if the length is fine and if the substring is actually the word
                if (i + len(w) <= len(s)) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                
                if dp[i]:
                    break

        return dp[0]