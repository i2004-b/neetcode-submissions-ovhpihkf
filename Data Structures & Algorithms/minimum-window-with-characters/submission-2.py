class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case: if t is longer than s, return an empty string
        if len(t) > len(s):
            return ""

        # Declare 2 hashmaps: 1 is for the count of T and another for the count of the window
        count_T, window = {}, {}

        # Iterate through t and add the counts of each of its letters
        for c in t:
            count_T[c] = 1 + count_T.get(c, 0)

        # Declare a have and need variable to keep track of the matches that need to be made
        have, need = 0, len(count_T) # Need is just the length of the count_T dictionary
        
        # Initialize the result pointers in an array of size 2 and the length to infinity
        res, res_len = [-1, -1], float("inf")

        # Declare a left pointer to shrink window size when needed
        l = 0

        # Iterate through s
        for r in range(len(s)):
            # Save the current character
            char = s[r]

            # Increment the count of the character in the window
            window[char] = 1 + window.get(char, 0)

            # Increment have if char is in count_T and the current value is == than that in count_T
            if char in count_T and window[char] == count_T[char]:
                have += 1

            # Iterate to shrink the window while have == need
            while have == need:
                # Update the length if needed
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                # Decrement the character at the left pointer in window
                window[s[l]] -= 1

                # Check to see if have should be decremented if the left value in count_T and window count has become less than count_T's vount
                if s[l] in count_T and window[s[l]] < count_T[s[l]]:
                    have -= 1

                # Increment the left pointer
                l += 1

        # Extract the pointers
        l, r = res
        # Return the string as long as one was found
        return s[l : r + 1] if res_len != float("inf") else ""


