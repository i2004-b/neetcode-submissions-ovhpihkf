class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Handle edge case if len(t) is greater than len(s) or it t is empty
        if len(t) > len(s) or t == "":
            return ""

        # Declare two empty hashsets
        countT, window = {}, {}

        # Initialize the T map (it won't be edited or changed for the rest)
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # Declare needed variables
        # Have will be at 0 as we will need to increment it
        have = 0
        # Need will be the number of distinct characters in t, regardless of count
        need = len(countT)

        # Initialize result indices and the length
        res, res_len = [-1, -1], float("inf")

        # Declare a left pointer
        l = 0

        # Iterate with r going through s
        for r in range(len(s)):
            # Get the current character
            c = s[r]
            # Add the character to the window
            window[c] = 1 + window.get(c, 0)

            # If the character is in count t and the numbers are equal, increment have
            if c in countT and window[c] == countT[c]:
                have += 1

            # Update the left pointer if have == need
            while have == need:
                # Update the length
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                # Need to move left, but before doing so decrement its value from the 
                window[s[l]] -= 1
                # Decrement have if s[l] in countT and if the value in window for that letter is < the value in countT
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                # Increment l
                l += 1

        # Get left and right bounds from res
        l, r = res
        # Return the string if one existed
        return s[l : r + 1] if res_len != float("inf") else ""