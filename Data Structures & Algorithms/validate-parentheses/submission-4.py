class Solution:
    def isValid(self, s: str) -> bool:
        # T: O(n), S: O(n)

        # Declare dictionary with matching closing and opening brackets
        match = {"}": "{", "]": "[", ")": "("}
        # Declare stack to hold opening brackets
        stack = []

        # Iterate through the string
        for char in s:
            if char in match:
                if not stack or match[char] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)

        return not stack    