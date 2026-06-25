class Solution:
    def decodeString(self, s: str) -> str:
        # T: O(n + N^2), S: O(n + N)
        # Stack to store the values of the stack
        stack = []

        for c in s:
            # Add everything that is not a closing bracket to the stack
            if c != "]":
                stack.append(c)
            # What to do when you hit an ending bracket
            else:
                # Keep track of the substring
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                
                # Pop the opening bracket
                stack.pop()

                # Keep track of the number
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
        
                # Add back to the stack
                stack.append(int(k) * substr)

        # Join stack and return string
        return "".join(stack)

