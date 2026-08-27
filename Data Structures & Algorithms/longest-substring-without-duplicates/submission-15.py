class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Keep track of result
        res = 0

        # Have hashmap to store where value were seen
        seen = {}

        # Pointer for left bound
        i = 0

        # Iterate through the string's characters
        for j in range(len(s)):
            # Check if the char is in the hashmap and within the bounds of the string
            if s[j] in seen and seen[s[j]] >= i:
                # Move i to where that character was seen
                i = seen[s[j]] + 1

            # Update location
            seen[s[j]] = j
            # Update result
            res = max(res, j - i + 1)

        return res