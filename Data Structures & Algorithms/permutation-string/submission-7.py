class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Length of s1 cannot be greater than s2
        if len(s1) > len(s2):
            return False

        # Create dictionary for s2 with characters and counts
        perm = {}

        for letter in s1:
            perm[letter] = 1 + perm.get(letter, 0)

        # Create left pointer
        l = 0
        window_size = len(s1)

        # Create window dictionary to hold the window
        window = {}

        # Iterate with right pointer
        for r in range(len(s2)):
            # Add item to the window
            window[s2[r]] = 1 + window.get(s2[r], 0)

            if r - l + 1 == window_size:
                if perm == window:
                    return True
                else:
                    # Decrement left value
                    window[s2[l]] -= 1
                    if not window[s2[l]]:
                        del window[s2[l]]
                    # Update l
                    l += 1

        return False