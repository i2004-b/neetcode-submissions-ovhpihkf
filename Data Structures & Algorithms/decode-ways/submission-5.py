class Solution:
    def numDecodings(self, s: str) -> int:
        # Declare two variables
        dp1, dp2 = 1, 0

        # Iterate backwards
        for i in range(len(s) - 1, -1, -1):
            # Check if the number is 0
            if s[i] == "0":
                curr = 0
            else:
                curr = dp1 # (i + 1)

            # Check if this can be made into two digits
            if (i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456"))):
                curr += dp2

            dp1, dp2 = curr, dp1

        return dp1