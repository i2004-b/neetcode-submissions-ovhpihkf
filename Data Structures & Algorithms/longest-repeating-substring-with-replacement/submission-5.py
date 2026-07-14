class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Solution 2 slightly optimized version

        # Declare a dictionary holding the count of the characters
        count = {}

        # Have a variable to store the length of the result
        res = 0

        # Have a variable to store the max frequency that is encountered
        max_freq = 0

        # Set l to 0
        l = 0

        # Iterate through the list using the r pointer
        for r in range(len(s)):
            # Update the count of the item at r
            count[s[r]] = 1 + count.get(s[r], 0)

            # Update max frequency if needed
            max_freq = max(max_freq, count[s[r]])

            # Check that the length is valid
            while (r - l + 1) - max_freq > k:
                # Move left pointer and update the counts of the items at the left
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)


        return res