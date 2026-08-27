class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check lengths of strings
        if len(s) != len(t):
            return False

        # Declare array to hold the counts of each
        count = [0] * 26

        # Iterate through the length of the strings
        for i in range(len(s)):
            # Update the locations (correspond to the letters)
            count[ord(s[i]) - ord("a")] += 1
            count[ord(t[i]) - ord("a")] -= 1

        # Iterate through array checking for non-zero values
        for cnt in count:
            if cnt != 0:
                return False

        return True