class Solution:
    def simplifyPath(self, path: str) -> str:
        # Need a stack to keep track of items
        stack = []
        # Track the current name of the directory
        curr = ""

        # Iterate through the path
        # Add a slash at the end in order to check the last element of the path
        for c in (path + "/"):
            # If item is a slash, you are at the end of a segment
            if c == "/":
                if curr == "..":
                    # Only pop if the stack is non empty
                    if stack:
                        stack.pop()
                elif curr != "" and curr != ".":
                    # Append the current directory to the stack
                    stack.append(curr)
                # Reset curr
                curr = ""
            # If not a slash, add the item to the list of curr
            else:
                curr += c

        # Return the stack joined with slashes, also add a slash at the beginning
        return "/" + "/".join(stack)