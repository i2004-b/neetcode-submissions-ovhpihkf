class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Word by word prefix check, using double for loops
        # Define the prefix to be the first word
        prefix = strs[0]

        # Compare every other word
        for w in range(1, len(strs)):
            # Set a counter to see how many similar letters the prefix and the current word have
            c = 0
            # Iterate over every letter in the new word
            # Make sure there are no out of bounds errors by using the min function
            for l in range(min(len(prefix), len(strs[w]))):
                # If not equal, break
                if prefix[l] != strs[w][l]:
                    break
                
                # Increment the counter if letters match
                c += 1

            # Update the prefix
            prefix = prefix[:c]

        # Return prefix
        return prefix
                    