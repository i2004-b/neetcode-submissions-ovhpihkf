class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = strs[0]

        for i in range(1, len(strs)):
            curr_prefix = []
            for j in range(min(len(strs[0]), len(strs[i]))):
                if strs[0][j] != strs[i][j]:
                    break
                curr_prefix.append(strs[i][j])
            
            if len(curr_prefix) < len(longest_prefix):
                longest_prefix = curr_prefix

        return "".join(longest_prefix)