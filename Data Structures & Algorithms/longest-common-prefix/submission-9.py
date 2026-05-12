class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Assign the initial prefix to the first string in the list
        prefix = strs[0]

        # Iterate through the remaining strings to compare to the prefix
        for i in range(1, len(strs)):
            # Iterate through each letter
            # Make sure to stop before an index error by taking the min of prefix or the current word
            match = 0
            for j in range(min(len(prefix), len(strs[i]))):
                # Break from this loop if letters are not equal
                if prefix[j] == strs[i][j]:
                    match += 1
                else:
                    break
            prefix = prefix[:match]

        # Return the prefix
        return prefix