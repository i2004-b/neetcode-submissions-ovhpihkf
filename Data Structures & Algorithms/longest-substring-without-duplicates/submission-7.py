class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}

        L, R = 0, 0
        longest = 0

        while R < len(s):
            if s[R] not in seen:
                seen[s[R]] = R
            else:
                if seen[s[R]] >= L:
                    L = seen[s[R]] + 1
                seen[s[R]] = R
            longest = max(longest, R - L + 1)
            
            R += 1

        return longest
