class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1, w2 = 0, 0

        merged = []

        while w1 < len(word1) and w2 < len(word2):

            if w1 == w2:
                merged.append(word1[w1])
                w1 += 1
            elif w2 < w1:
                merged.append(word2[w2])
                w2 += 1

        merged.append(word1[w1:])
        merged.append(word2[w2:])

        return "".join(merged)