class Solution:
    def decodeString(self, s: str) -> str:
        # T: O(n + N), S: O(n + N)

        # Two stacks: one holds the strings and the other the k-value
        string_stack = []
        count_stack = []
        # Set curr to empty string and k to 0
        curr = ""
        k = 0

        # Iterate through the string
        for c in s:
            """
            4 Cases:
            - digit: update k
            - opening bracket: add items to respective stacks
            - closing bracket: pop from stacks and make the updated substr
            - any other character: update curr
            """
            if c.isdigit():
                k = k * 10 + int(c)
            elif c == "[":
                string_stack.append(curr)
                count_stack.append(k)
                # Reset curr and k
                curr = ""
                k = 0
            elif c == "]":
                # Set the current substring to a temp variable
                temp = curr
                # Set curr to popped value from string_stack
                curr = string_stack.pop()
                # Pop from count_stack to get count
                count = count_stack.pop()
                # Update substring
                curr += temp * count
            else:
                # Update curr
                curr += c
        
        # Return curr
        return curr