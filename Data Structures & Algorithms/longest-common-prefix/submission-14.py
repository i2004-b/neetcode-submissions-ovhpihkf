class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Word by word prefix check, using a for and then a while loop
        # Set prefix to the first word
        prefix = strs[0]

        # Iterate over every word in the array besides the first one
        for w in range(1, len(strs)):
            # Set counter for the while loop
            l = 0
            # Iterate while l is less than the minimum of the length of the prefix or the length of the current word
            # You want the minimum to avoid any out of bounds errors
            while l < min(len(prefix), len(strs[w])):
                # If there is mismatch, break
                if strs[w][l] != prefix[l]:
                    break
                
                # Increment the counter
                l += 1

            # Update the prefix
            prefix = prefix[:l]

        # Return the prefix
        return prefix