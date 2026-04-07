class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Declare hashmap to store frequencies
        freq = {}
        # Declare variable to hold max length
        maxLen = 0
        # Declare two pointers
        L, R = 0, 0

        # Iterate through the length of the list
        while R < len(s):
            # Add to the frequency of the item in the hashmap
            freq[s[R]] = 1 + freq.get(s[R], 0)
            # Calculate difference to see how many items need to be replaced
            diff = (R - L + 1) - max(freq.values())

            # Loop and update the left pointer if too many values need to be replaced
            while diff > k:
                # Decrement the frequency of the item left is at before moving left
                freq[s[L]] -= 1
                # Update left pointer
                L += 1
                # Re-calculate difference
                diff = (R - L + 1) - max(freq.values())

            # Update the max length
            maxLen = max(maxLen, R - L + 1)
            # Increment R
            R += 1

        return maxLen
