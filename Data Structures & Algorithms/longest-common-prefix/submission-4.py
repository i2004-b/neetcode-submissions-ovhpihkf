class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Horizontal Scanning without creating new string
        prefix = strs[0]

        # Iterate through the rest of the strings and compare with strs[0]
        for i in range(1, len(strs)):
            # Count number of characters in common for each word with strs[0]
            j = 0
            # Iterate through min of every letter in each word or the length of the strs[0]
            for k in range(min(len(prefix), len(strs[i]))):
                # Stop counting the current prefix if there is a mismatch
                if strs[i][k] != prefix[k]:
                    break
                # Add to j if there is a match
                j += 1

            # Update prefix, will not be longer than strs[0]
            prefix = prefix[:j]

        return prefix