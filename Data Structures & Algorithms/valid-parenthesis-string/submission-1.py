class Solution:
    def checkValidString(self, s: str) -> bool:
        # Declare two stacks: one for open parenthesis and one for the wild cards
        left = []
        wild = []

        # Iterate through the string 
        for ind, c in enumerate(s):
            # Check if left and add index to stack
            if c == "(":
                left.append(ind)
            elif c == "*":
                wild.append(ind)
            else:
                # Check if both are empty, in which case return False
                if not left and not wild:
                    return False

                if left:
                    left.pop()
                elif wild:
                    wild.pop()

        # Iterate through stacks to match any remaining left characters
        while left and wild:
            # If the index of the left is greater than the wild, it cannot be matched, so return False
            if left.pop() > wild.pop():
                return False

        return not left