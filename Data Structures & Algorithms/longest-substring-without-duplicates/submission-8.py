class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Dictionary to hold the seen characters and where they were seen
        seen = {}
        # Pointers to move the window
        L, R = 0, 0
        # Track the max length, that starts out being 0
        maxLen = 0

        while R < len(s):
            # Put in dictionary if not seen before
            if s[R] not in seen:
                seen[s[R]] = R
            else:
                # Only move L if the repeat letter was seen in the current substring
                if seen[s[R]] >= L:
                    L = seen[s[R]] + 1
                # Update with the new location in dictionary
                seen[s[R]] = R

            # Recalculate the maxlength
            maxLen = max(maxLen, R - L + 1)

            # Increment R
            R += 1

        # Return the max length
        return maxLen