class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check the lengths
        if len(s) != len(t):
            return False
        
        # Initialize array
        anagram = [0] * 26

        # Increment and decrement
        # Use ord("a") as the base
        for i in range(len(s)):
            anagram[ord(s[i]) - ord("a")] += 1
            anagram[ord(t[i]) - ord("a")] -= 1

        # Check that the values are all 0
        for val in anagram:
            if val != 0:
                return False

        return True