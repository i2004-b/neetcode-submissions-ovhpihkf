class Solution:

    def encode(self, strs: List[str]) -> str:
        # Declare empty list for values
        res = []

        # Iterate through the words
        for word in strs:
            # Append length of string
            res.append(str(len(word)))
            res.append("#")
            res.append(word)
        
        # Return the string
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        # Result with words
        res = []

        # Pointer to go through list
        i = 0

        # Iterate through the length of encoded strings
        while i < len(s):
            # Pointer to find where the word starts
            j = i

            # Iterate to find the end of the length of the word
            while s[j] != "#":
                j += 1

            # The length is starting from i and goes up to (but not through) where j ends
            length = int(s[i : j])

            # Get the word, starting at index j + 1 (# is at index j) and going through the length
            word = s[j + 1 : j + 1 + length]
            
            # Add the word to the result
            res.append(word)

            # Update i to be at the start of the next digit (or at the end if this was the last word)
            i = j + 1 + length

        return res