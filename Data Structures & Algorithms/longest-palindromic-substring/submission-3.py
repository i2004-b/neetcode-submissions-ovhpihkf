class Solution:
    def longestPalindrome(self, s: str) -> str:
        # DP Solution
        # Want to set up a 2D grid to hold if values in btwn are the same
        # Edge case: if length 1 and 2: palindorm; if length 3 and edge letters are the same: palindrome

        # Get the length of string
        n = len(s)

        # Create grid filled with False
        dp = [[False] * n for _ in range(n)]

        # Track the longest length and the starting index
        resIdx = 0
        resLen = 0

        # Iterate backwards
        for i in range(n - 1, -1, -1):
            # Iterate from i to the end
            for j in range(i, n):
                # Check the following:
                # A) Are letters at i and j equal and B) check if it is one of the edge cases or the section btn if a palindrome
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    # Set location to True
                    dp[i][j] = True

                    # Check if longest
                    if j - i + 1 > resLen:
                        resLen = j - i + 1
                        resIdx = i

        return s[resIdx : resIdx + resLen]