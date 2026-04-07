class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L, curr_size, max_size = 0, 0, 0

        seen = {}

        for R in range(len(s)):
            if s[R] not in seen:
                seen[s[R]] = R
                curr_size = R - L + 1
            else:
                if seen[s[R]] >= L:
                    L = seen[s[R]] + 1
                seen[s[R]] = R
                curr_size = R - L + 1
            max_size = max(max_size, curr_size)

        return max_size
