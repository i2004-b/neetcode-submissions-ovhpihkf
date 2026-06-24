class Solution:
    def simplifyPath(self, path: str) -> str:
        # Split the directory path
        dirs = path.split("/")
        # Have a stack to hold the directories and files in simplified path
        stack = []

        # Iterate through the directory items
        for item in dirs:
            # If the command is to go to previous/parent directory, check also if stack is existent
            if item == "..":
                # Pop from stack if other elements within stack
                if stack:
                    stack.pop()
            # Add items as long as they are not spaces (product of using split and having / in it) and the period
            elif item != "" and item !=".":
                stack.append(item)

        # Add a slash to the beginning
        return "/" + "/".join(stack)