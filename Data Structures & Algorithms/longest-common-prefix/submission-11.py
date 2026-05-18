class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Column by Column method using the join method

        # Store the result prefix
        res = []

        # Iterate through the letters of the first word and compare with every other word
        for index in range(len(strs[0])):
            # Iterate through every word
            for word in strs:
                # Break out and return if there is an out of bounds error or mismatch
                # Check if the index is LONGER than the word you are checking, not the original one
                # If strings are longer, you won't encounter any issues as the outer loop iterates for the length of strs[0]
                if index == len(word) or word[index] != strs[0][index]:
                    return "".join(res)

            # Add the common letter to the string
            res.append(word[index])

        # Return the result
        return "".join(res)