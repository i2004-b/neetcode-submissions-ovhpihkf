class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        # Iterate through the rest of the strings
        for i in range(1, len(strs)):
            # Set a counter to keep track of how many letters match
            j = 0
            # Iterate through the minimum length to avoid an out of bounds error
            while j < min(len(prefix), len(strs[i])):
                if prefix[j] != strs[i][j]:
                    break

                j += 1

            prefix = prefix[: j]
        
        return prefix