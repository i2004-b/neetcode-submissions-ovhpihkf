class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        for letter in range(len(s)):
            countS[s[letter]] = 1 + countS.get(s[letter], 0) # Default value
            countT[t[letter]] = 1 + countT.get(t[letter], 0)
        
        for char in countS:
            if countS[char] != countT.get(char, 0): # To ensure that if key DNE, no error thrown
                return False

        return True

        