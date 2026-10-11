class Solution:
    def checkValidString(self, s: str) -> bool:
        # Two stacks
        left = []
        wild = []

        # Iterate through the string 
        for ind, val in enumerate(s):
            if val == "(":
                left.append(ind)
            elif val == "*":
                wild.append(ind)
            else:
                # If right cannot be matched, return False
                if not left and not wild:
                    return False

                if left:
                    left.pop()
                elif wild:
                    wild.pop()

        while left and wild:
            if left.pop() > wild.pop():
                return False

        return not left