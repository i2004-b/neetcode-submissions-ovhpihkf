class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        letters = {}
        for i in range(len(s1)):
            letters[s1[i]] = 1 + letters.get(s1[i], 1)
        

        # permutation will be in fixed window size
        L, R = 0, len(s1) - 1

        while R < len(s2):
            window = {}
            for i in range(len(s1)):
                window[s2[L + i]] = 1 + window.get(s2[L + i], 1)
            
            if window == letters:
                return True

            L, R = L + 1, R + 1

        return False