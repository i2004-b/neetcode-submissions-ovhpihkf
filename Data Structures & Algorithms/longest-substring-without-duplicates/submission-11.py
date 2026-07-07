class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        locations = {}

        l = 0

        for r in range(len(s)):
            if s[r] in locations and locations[s[r]] >= l:
                l = locations[s[r]] + 1
            
            length = max(length, r - l + 1)

            locations[s[r]] = r





        return length