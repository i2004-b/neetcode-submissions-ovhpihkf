class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # "Column by Column" Method

        # Intialize the result
        res = ""

        # Simultaneously iterate through ALL of the strings for each letter
        # Arbitrarily choose the first word in the array
        for index in range(len(strs[0])):
            # Check each index one at a time for each word
            for word in strs:
                # Break out and return if there is an index error or mismatch
                # If the index equals the length of the current string, that would cause out of bounds error
                if index == len(word) or word[index] != strs[0][index]:
                    return res
                
            # Add the current letter to the result
            res += word[index]

        # Return the result
        return res