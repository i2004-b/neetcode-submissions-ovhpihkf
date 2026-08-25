class Solution:
    def countSubstrings(self, s: str) -> int:
        # DP: T - O(n^2) and S - O(n^2)
        # Get length of string
        n = len(s)

        # Set result counter
        res = 0

        # Create dp array to hold if palindrome
        dp = [[False] * n for _ in range(n)]

        # Iterate backwards
        for i in range(n - 1, -1, -1):
            # Iterate from position of i to the end
            for j in range(i, n):
                # Check if palindrome
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    # Set location to True
                    dp[i][j] = True
                    # Update result
                    res += 1


        return res