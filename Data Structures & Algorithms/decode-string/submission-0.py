class Solution:
    def decodeString(self, s: str) -> str:
        # Declare a stack to hold values of string
        stack = []

        # Iterate through the characters in the string
        for i in range(len(s)):
            # If the character is not a closing bracket, add it to the stack
            if s[i] != "]":
                stack.append(s[i])
            else:
                # Create substring of the letters until the opening bracket
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                
                # Pop the opening bracket
                stack.pop()

                # Obtain the number of repetitions (similar to getting substring)
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k

                # Append the sequence repeated k times to the stack
                stack.append(int(k) * substr)

        # Join the elements in the stack (decoded)
        return "".join(stack)