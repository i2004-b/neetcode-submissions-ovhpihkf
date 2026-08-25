class Solution:
    def countSubstrings(self, s: str) -> int:
        # Two pointers method: T - O(n^2) and S - O(1)

        # Basic Idea: iterate through each point, treating as the center
        # Check both the palindromes that are odd length and even length

        # Track result
        res = 0

        for i in range(len(s)):
            # Odd, set l and r to be at the same spot at first
            l, r = i, i

            # Check that they are in range 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # Add to result
                res += 1
                # Move pointers
                l, r = l - 1, r + 1

            # Even
            l, r = i, i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l, r = l - 1, r + 1

        return res
