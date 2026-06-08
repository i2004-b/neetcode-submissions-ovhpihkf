class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        # Helper function to figure out if a palindrome
        def is_palin(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                
                l, r = l + 1, r - 1

            return True


        # Declare pointers
        l, r = 0, len(s) - 1

        # Iterate while l does not pass r
        while l < r:
            # If the letters are not equal, run the function and return if either way is a palindrome
            if s[l] != s[r]:
                return is_palin(s, l, r - 1) or is_palin(s, l + 1, r)

            l += 1
            r -= 1

        return True
        