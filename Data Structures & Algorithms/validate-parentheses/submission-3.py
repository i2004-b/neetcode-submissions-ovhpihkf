class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {")": "(", "}": "{", "]": "["}
        opened = []

        for bracket in s:
            if bracket in hashMap:
                if opened and hashMap[bracket] == opened[-1]:
                    opened.pop()
                else:
                    return False
            else:
                opened.append(bracket)

        return not opened
        