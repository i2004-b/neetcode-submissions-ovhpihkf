class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l, r = 0, 0
        arr = []

        while l < len(word1) and r < len(word2):
            arr.append(word1[l])
            arr.append(word2[r])

            l, r = l + 1, r + 1

            while l == len(word1) and r < len(word2):
                arr.append(word2[r])
                r += 1
            while r == len(word2) and l < len(word1):
                arr.append(word1[l])
                l += 1

        return "".join(arr)
