class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 2 Pointer Solution

        # Set result length and result starting index to 0
        resInd = 0
        resLen = 0

        # Iterate for each letter in the string to treat it as the middle
        for i in range(len(s)):
            # Odd length palindrome
            # Set l and r to start at i 
            l, r = i, i

            # Check that l and r are in bounds AND that they are equal
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # If the length if lonegr, update results and index
                if (r - l + 1) > resLen:
                    resInd = l
                    resLen = r - l + 1

                # Update pointers
                l, r = l - 1, r + 1

            # Even length palindrome
            # Set l and r to start one apart from each other
            l, r = i, i + 1

            # Same logic as before
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resInd = l
                    resLen = r - l + 1

                l, r = l - 1, r + 1

        return s[resInd: resInd + resLen]