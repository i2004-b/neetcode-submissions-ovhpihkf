class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the length is not the same, they cannot be anagrams.
        if len(s) != len(t):
            return False

        s_letters = {}
        t_letters = {}

        for letter in s:
            s_letters[letter] = 1 + s_letters.get(letter, 0)

        for letter in t:
            t_letters[letter] = 1 + t_letters.get(letter, 0)

        return s_letters == t_letters