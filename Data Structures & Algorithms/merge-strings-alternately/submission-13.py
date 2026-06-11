class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Single Pointer version
        
        # Hold the letters
        arr = []

        # Lengths of the words
        w1, w2 = len(word1), len(word2)

        for i in range(max(w1, w2)):
            if i < w1:
                arr.append(word1[i])
            if i < w2:
                arr.append(word2[i])

        return "".join(arr)