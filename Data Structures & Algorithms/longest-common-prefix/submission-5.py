class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Vertical scanning method checking each letter
        # Arbitrarily pick strs[0] as the longest.
        # Iterate through each letter
        for i in range(len(strs[0])):
            # Iterate through each string at position i
            for s in strs:
                # Break and return if out of bounds or there is a mismatch
                if i == len(s) or s[i] != strs[0][i]:
                    return strs[0][:i]

        # If it executed without breaking, just return strs[0]
        return strs[0]