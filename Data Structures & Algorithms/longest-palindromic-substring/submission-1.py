class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 2 Pointer Solution

        # Set result length and result starting index to 0
        self.resInd = 0
        self.resLen = 0

        # Helper function to check if palindrome
        def palindrome(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > self.resLen:
                    self.resLen = r - l + 1
                    self.resInd = l

                # Update pointers 
                l, r = l - 1, r + 1

        # Iterate for each letter in the string to treat it as the middle
        for i in range(len(s)):
            # Odd length palindrome
            # Set l and r to start at i 
            l, r = i, i

            # Check that l and r are in bounds AND that they are equal
            palindrome(l, r)

            # Even length palindrome
            # Set l and r to start one apart from each other
            l, r = i, i + 1

            # Same logic as before
            palindrome(l, r)

        return s[self.resInd: self.resInd + self.resLen]