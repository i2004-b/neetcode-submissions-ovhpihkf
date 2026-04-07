class Solution:
    def isValid(self, s: str) -> bool:

        # Empty stack to store opening characters
        open_chars = []

        # Hash-map that maps closing to opening
        matchSymbol = {")": "(", "}": "{", "]": "["}

        for symbol in s:
            if symbol in matchSymbol:
                if open_chars and matchSymbol[symbol] == open_chars[-1]:
                    open_chars.pop()
                else:
                    return False
            else:
                open_chars.append(symbol)

        return not open_chars