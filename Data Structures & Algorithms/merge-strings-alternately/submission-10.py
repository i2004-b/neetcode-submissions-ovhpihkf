class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Declare array to hold letters the join
        arr = []

        # Declare pointers pointing to each word first letter
        i, j = 0, 0

        # Iterate while both pointers in range of the words
        while i < len(word1) and j < len(word2):
            arr.append(word1[i])
            arr.append(word2[j])

            i, j = i + 1, j + 1

        # Add remaining characters
        while i < len(word1):
            arr.append(word1[i])
            i += 1
        
        while j < len(word2):
            arr.append(word2[j])
            j += 1

        return "".join(arr)