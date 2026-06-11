class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Declare empty array to hold letters
        arr = []

        # Have two pointers pointing to the start of the words
        i, j = 0, 0

        # Iterate while either one of the pointers is still in range
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                arr.append(word1[i])
                i += 1
            
            if j < len(word2):
                arr.append(word2[j])
                j += 1

        return "".join(arr)