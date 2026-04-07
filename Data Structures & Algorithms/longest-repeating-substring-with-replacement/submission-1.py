class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Make dictonary
        freq = {}

        # Pointers
        l, r = 0, 0

        # Max length
        max_len = 0

        # Iterate through the string
        for r in range(len(s)):
            # Add the current value to the dictionary
            freq[s[r]] = 1 + freq.get(s[r], 0)

            # Check whether the length adheres to the standards discussed
            while ((r - l + 1) - max(freq.values())) > k:
                # Update the dictionary
                freq[s[l]] -= 1
                # Increment l by 1 so that you can shift the window size
                l += 1

            # Update the max_len variable
            max_len = max(max_len, r - l + 1)

        return max_len
