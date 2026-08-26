class Solution:
    def numDecodings(self, s: str) -> int:
        # Create a cache with the length set to 1 (handles any empty strings we may deal with)
        dp = {len(s): 1}

        # Have dfs function taking as input the index
        def dfs(i):
            # Base case 1: if the value exists in cache, return it
            if i in dp:
                return dp[i]
            # Base case 2: if the value is a 0, return 0
            if s[i] == "0":
                return 0

            # Get the number of decodings if this is a single digit (run on the rest)
            res = dfs(i + 1)

            # Check if you can make it a two-digit number
            # First: check that the i + 1 is in bounds
            # Second: check the first digit
            #   If first digit is 1 or first digit is a 2 with the second being 0-6, call dfs

            if (i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456"))):
                res += dfs(i + 2) # Made into a two digit number and checking the rest

            # Update dp
            dp[i] = res

            # Return res
            return res

        # Run dfs at 0
        return dfs(0)