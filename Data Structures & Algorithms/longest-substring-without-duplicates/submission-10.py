class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        duplicates = {}
        max_len = 0
        l = 0

        for r in range(len(s)):
            if s[r] in duplicates:
                if duplicates[s[r]] >= l:
                    l = duplicates[s[r]] + 1

            duplicates[s[r]] = r
            max_len = max(r - l + 1, max_len)

        return max_len