class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Solution using a set
        # T: O(n), S: O(n)
        # For the set, you need an extra loop within the for loop as you don't know the indices where letters occurred at
        # You iterate until you have passed the original version with the left pointer

        # Declare set
        char_set = set()
        # Declare a pointer to the left
        l = 0
        # Declare a variable to hold the result
        res = 0

        # Iterate through list (acts as right pointer)
        for r in range(len(s)):
            # Have a while loop to remove characters from the set if you encounter duplicate
            while s[r] in char_set:
                # Remove the value at l
                char_set.remove(s[l])
                # Update l
                l += 1

            # Add new values to the char_set
            char_set.add(s[r])

            # Update the result
            res = max(res, r - l + 1)

        # Return the result
        return res