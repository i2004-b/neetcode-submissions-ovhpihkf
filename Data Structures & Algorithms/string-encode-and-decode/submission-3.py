class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []

        for word in strs:
            # Append the string of the length of the word
            encoded.append(str(len(word)))
            # Append a delimiter
            encoded.append("#")
            # Append the word itself
            encoded.append(word)

        # Join the strings in the array to make one string
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        words = []

        # Pointer to iterate through s
        i = 0
        while i < len(s):
            # Declare j to point to where i is pointing at the beginning
            # Its job is to find the length
            j = i

            while s[j] != "#":
                j += 1

            # Get the length of the word
            length = int(s[i:j])

            # Get the word
            word = s[j + 1: j + 1 + length]

            words.append(word)
            
            # Update i
            i = j + 1 + length

        return words

