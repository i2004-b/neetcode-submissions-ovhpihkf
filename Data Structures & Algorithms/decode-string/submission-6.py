class Solution:
    def decodeString(self, s: str) -> str:
        """
        Method 2:
        T: O(n + N)
        S: O(n + N)

        Use two stacks
        One stack to store the numbers and another to store the letters
        Add to the appropriate stack when you hit the [
        Keep track of the current string
        Keep track of the current number
        when you get to ], pop and append to the current
        """

        char_stack = []
        count_stack = []
        curr = ""
        k = 0

        # Iterate through the characters in the string
        for c in s:
            if c.isdigit():
                k = k * 10 + int(c)
            elif c == "[":
                char_stack.append(curr)
                count_stack.append(k)
                curr = ""
                k = 0
            elif c == "]":
                # Save the current string
                tmp = curr
                count = count_stack.pop()
                curr = char_stack.pop()
                curr += count * tmp


            else:
                curr += c
        
        return curr
        