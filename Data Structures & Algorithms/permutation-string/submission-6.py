class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Add letters of the word you are trying to permute
        letters = {}

        for letter in s1:
            letters[letter] = 1 + letters.get(letter, 0)

        l, r = 0, 0

        window = {}
        for r in range(len(s2)):
            window[s2[r]] = 1 + window.get(s2[r], 0)
            
            if r - l + 1 == len(s1):
                if window == letters:
                    return True

                window[s2[l]] -= 1
                if not window[s2[l]]:
                    window.pop(s2[l])

                l += 1

            

        return False
