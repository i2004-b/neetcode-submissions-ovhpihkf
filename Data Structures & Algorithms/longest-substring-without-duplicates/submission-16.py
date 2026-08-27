class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Attempt with set
        res = 0

        seen = set()

        # Leftbound pointer
        l = 0

        # Iterate through the string
        for r in range(len(s)):
            # Check if the s[r] value is in the set and if it is, keep removing elements that are at l (increment l) while s[r] remains
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            # Add new item to the set
            seen.add(s[r])
            # Calculate length
            res = max(res, r - l + 1)

        return res


        