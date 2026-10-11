class Solution:
    def checkValidString(self, s: str) -> bool:
        # Have two variables to track 
        left_min = left_max = 0

        # Iterate through the string 
        for val in s:
            if val == "(":
                left_min += 1
                left_max += 1
            elif val == ")":
                left_min -= 1
                left_max -= 1
            else:
                left_min -= 1
                left_max += 1

            # Check if left_max below 0
            if left_max < 0:
                return False
            left_min = max(0, left_min)

        return not left_min