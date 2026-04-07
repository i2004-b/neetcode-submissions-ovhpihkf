class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string_1 = Counter(s)
        string_2 = Counter(t)
        return string_1 == string_2