class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split("/")
        stack = []

        for item in dirs:
            if item == "..":
                if stack:
                    stack.pop()
            elif item != "" and item !=".":
                stack.append(item)

        return "/" + "/".join(stack)