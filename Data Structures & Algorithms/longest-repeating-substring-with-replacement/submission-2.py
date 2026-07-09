class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Solution 1: T: O(26 * n) = O(n), S: O(n)

        # Declare a hashmap to hold the count of chars in string
        count = {}

        # Track the result
        res = 0

        # Declare left pointer
        l = 0

        # Iterate through the list
        for r in range(len(s)):
            # Update the count of the current character
            count[s[r]] = 1 + count.get(s[r], 0)

            # If the length of the substring - max_freq in count is > the number of replacements (k),
            # need to decrement value at l and then increment l

            while (r - l + 1) - max(count.values()) > k:
                # Decrement item at the left
                count[s[l]] -= 1
                # Increment left
                l += 1

            # Update result
            res = max(res, r - l + 1)

        return res