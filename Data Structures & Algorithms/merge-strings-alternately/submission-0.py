class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0

        merged = ""

        while i < len(word1) and j < len(word2):
            if i == j:
                merged += word1[i]
                i += 1
            elif j < i:
                merged += word2[j]
                j += 1

        while i < len(word1):
            merged += word1[i]
            i += 1
        
        while j < len(word2):
            merged += word2[j]
            j += 1

        return merged
