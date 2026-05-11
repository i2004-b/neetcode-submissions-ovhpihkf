class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)

        if len_s != len_t:
            return False

        s_char = {}
        t_char = {}

        for i in range(len_s):
            s_char[s[i]] = 1 + s_char.get(s[i], 0)
            t_char[t[i]] = 1 + t_char.get(t[i], 0)

        return True if s_char == t_char else False