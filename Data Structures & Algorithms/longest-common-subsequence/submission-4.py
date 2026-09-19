class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Store the longest lengths in some sort of data structure
        # Make a row prefilled with all zeros that is one longer than the number of columns
        # Make whichever word is shorter column 1
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        # Number of columns based on the shorter 1 (text2)
        # Have an extra column
        dp = [0] * (len(text2) + 1)

        # Iterate through the letters in text 1
        for i in range(len(text1)):
            # Track the current row
            row = [0] * (len(text2) + 1)
            # Iterate through the letters in text2
            for j in range(len(text2)):
                # Check if the letters are the same
                if text1[i] == text2[j]:
                    row[j + 1] = 1 + dp[j]
                else:
                    row[j + 1] = max(dp[j + 1], row[j])

            dp = row

        return dp[-1]
