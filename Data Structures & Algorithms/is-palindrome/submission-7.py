class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Set pointers to the beginning and the end
        l, r = 0, len(s) - 1

        # Iterate while l < r
        while l < r:
            # Iterate to make sure that l is at a letter but check if l < r (so l does not pass r)
            while l < r and not s[l].isalnum():
                l += 1
            
            # Iterate to make sure that r is at a letter but check l < r (so l is not ahead of r)
            while l < r and not s[r].isalnum():
                r -= 1
            
            # Check if the letters (lowercased) are not equal
            if s[l].lower() != s[r].lower():
                return False

            # Increment l and decrement r
            l, r = l + 1, r - 1

        # Return True
        return True