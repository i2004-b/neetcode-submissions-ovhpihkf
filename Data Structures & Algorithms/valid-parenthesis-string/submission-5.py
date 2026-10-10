class Solution:
    def checkValidString(self, s: str) -> bool:
        
        """
        only contains (, ), *

        left must come before right
        * wildcard --> can be left, right, or empty
        
        (( ** )

        Recursively:
        iterate through the string 
        check what type of item it is
        keep a count of the opening and closings that you have
        for every wildcard, go down all three paths (is it open, closed, or empty string)
        Because of the three choices for the wildcard this would turn into a very inefficient problem to solve recursively (O(3 ^ n))

        Could use stacks
        Use two stacks --> one storing the open brackets and another wildcard
        you iterate through the string
        if it is an open bracket, you add it to the thing
        if it is a wildcard, you add it to its own stack
        if it is a closed bracket your open and wild list is empty, return false
        pop from the open if it exists
        else pop from the wild

        You want to pop in the indices so you can keep track

        After that, open and wildcard may have characters
        if open is greater than the wildcard: return false

        pop from both (continuously)
        if wildcard runs out before, return false

        return true

        
        """

        left = []
        wild = []

        for ind, char in enumerate(s):
            if char == "(":
                left.append(ind)
            elif char == "*":
                wild.append(ind)
            else:
                if not left and not wild:
                    return False

                if left:
                    left.pop()
                else:
                    wild.pop()
        
        while left and wild:
            if left.pop() > wild.pop():
                return False

        return not left

    