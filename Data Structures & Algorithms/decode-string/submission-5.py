class Solution:
    def decodeString(self, s: str) -> str:
        """
        Method 1:
        T: O(n + N^2)
        S: O(n + N)
        """
        
        stack = []

        # Iterate through the whole array
        # Put every value into the array
        # Unless its closing bracket

        for c in s:
            if c != "]":
                stack.append(c)
            else:
                sub = ""
                while stack[-1] != "[":
                    sub = stack.pop() + sub

                stack.pop()

                count = ""
                while stack and stack[-1].isdigit():
                    count = stack.pop() + count

            # Add the word back to the stack
                stack.append(int(count) * sub)
        
        return "".join(stack)
                
