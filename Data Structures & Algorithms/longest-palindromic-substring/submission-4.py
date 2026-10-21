class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        length = 0
        sub = ""

        for i in range(len(s)):
            l, r = i, i

            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if r - l + 1 > length:
                        length = r - l + 1
                        sub = s[l:r + 1]
                    l, r = l - 1, r + 1
                else:
                    break

        for i in range(len(s)):
            l, r = i - 1, i

            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if r - l + 1 > length:
                        length = r - l + 1
                        sub = s[l:r + 1]
                    l, r = l - 1, r + 1
                else:
                    break

        return sub
        