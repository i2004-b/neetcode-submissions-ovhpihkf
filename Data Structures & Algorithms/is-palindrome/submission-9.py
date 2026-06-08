class Solution:
    def isPalindrome(self, s: str) -> bool:
        # WITH OWN ALPHANUM FUNCTION
        # Set pointers to the beginning and the end
        l, r = 0, len(s) - 1

        # Iterate while l < r
        while l < r:
            # Iterate to make sure that l is at a letter but check if l < r (so l does not pass r)
            while l < r and not self.alphanum(s[l]):
                l += 1
            
            # Iterate to make sure that r is at a letter but check l < r (so l is not ahead of r)
            while l < r and not self.alphanum(s[r]):
                r -= 1
            
            # Check if the letters (lowercased) are not equal
            if s[l].lower() != s[r].lower():
                return False

            # Increment l and decrement r
            l, r = l + 1, r - 1

        # Return True
        return True 

    def alphanum(self, n):
        return ((0 <= ord(n) - ord("A") <= 26) or (0 <= ord(n) - ord("a") < 26) or (0 <= ord(n) - ord("0") < 10))