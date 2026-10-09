class Solution:
    def checkValidString(self, s: str) -> bool:
        # Have two variables to track
        leftMin, leftMax = 0, 0

        # Subtract from both when right; add to both when left; when wildcard, subtract from min, add to max

        for c in s:
            if c == "(":
                leftMin += 1
                leftMax += 1
            elif c == ")":
                leftMin -= 1
                leftMax -= 1
            else:
                leftMin -= 1
                leftMax += 1

            # If leftMax is negative, then return False
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0

        return leftMin == 0