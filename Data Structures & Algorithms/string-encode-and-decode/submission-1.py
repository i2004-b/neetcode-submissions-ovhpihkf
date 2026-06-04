class Solution:

    def encode(self, strs: List[str]) -> str:
        # Have an array to hold the encoded strings (that will be joined together later to make a string)
        strings = []

        # Iterate through each word
        for word in strs:
            # Length of the word
            length = len(word)
            strings.append(str(length)) # Avoids any errors that may be thrown by join
            # Append a pound sign as the delimiter
            strings.append("#")
            # Append the letters in the word
            # for letter in word:
                # strings.append(letter)
            strings.append(word)

        # Return the joined array
        return "".join(strings)

    def decode(self, s: str) -> List[str]:
        # The result will be a list of strings
        res = []
        # Have a pointer i telling us where we are in the input string
        i = 0

        # Iterate character by character while in bounds
        while i < len(s):
            # The first position will be an integer
            j = i
            # Find the delimited "#"
            while s[j] != "#":
                # Increment j by 1
                j += 1
            
            # At j at this point, it is the delimiter
            # Find the length of the word using the digit
            length = int(s[i : j]) # Go up to j, not through because j is "#"

            # Append the word to the res array
            res.append(s[j + 1: j + 1 + length]) # Start at j + 1 to ignore delimiter
            # Set i to be at the beginning of the next digit or possibly the end of the string
            i = j + 1 + length

        # Return the result
        return res
