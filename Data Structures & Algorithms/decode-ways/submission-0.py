class Solution:
    def numDecodings(self, s: str) -> int:
        # CACHE: T, S: O(1)
        # Make cache, initialized with the length of the string being 1

        dp = {len(s): 1}

        # Declare dfs function
        # Pass in index
        def dfs(i):
            # Base case 1: if the value is in the cache, return int
            if i in dp:
                return dp[i]
            # Base case 2: if the value is 0, return 0
            if s[i] == "0":
                return 0

            # Set the result from this point to be based on dfs from the next location
            res = dfs(i + 1)

            # Check if this can be made into 2-digit
            # Check if it is inbounds
            # Check the first digit
                # If it is a 1, you're good
                # If it is a 2 and the second digit is between 0 and 6, you're good
            if (i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456"))):
                # Add to result
                res += dfs(i + 2)

            # Update dp
            dp[i] = res

            return res

        # Run dfs
        return dfs(0)
