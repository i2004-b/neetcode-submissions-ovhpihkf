class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindrome(s):
            l, r = 0, len(s) - 1

            while l < r:
                if s[l] != s[r]:
                    return False

                l, r = l + 1, r - 1

            return True

        L, R = 0, len(s) - 1

        while L < R:
            if s[L] != s[R]:
                return palindrome(s[L + 1: R + 1]) or palindrome(s[L: R])

            L, R = L + 1, R - 1

        return True