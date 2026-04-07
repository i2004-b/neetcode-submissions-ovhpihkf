class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return (self.isPalindrome(s, l + 1, r) or 
                        self.isPalindrome(s, l, r - 1))
            
            l += 1
            r -= 1

        return True
    
    def isPalindrome(self, string, left, right):
        while left < right:
            if string[left] != string[right]:
                return False

            left += 1
            right -= 1

        return True

        