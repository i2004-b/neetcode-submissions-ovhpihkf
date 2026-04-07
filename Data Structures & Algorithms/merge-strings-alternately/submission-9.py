class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        i, j = 0, 0

        w1 = len(word1)
        w2 = len(word2)

        while i < w1 or j < w2:
            if i < w1:
                merged.append(word1[i])
                i += 1

            if j < w2:
                merged.append(word2[j])
                j += 1

        return "".join(merged)