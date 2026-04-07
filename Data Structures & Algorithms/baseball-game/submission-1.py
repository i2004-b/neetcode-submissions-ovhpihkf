class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # Time: O(n)
        # Space: O(n)
        # Declare stack
        stack = []
        result = 0

        # Iterate through operations
        for op in operations:
            if op == "+":
                result += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                result += stack[-1] * 2
                stack.append(stack[-1] * 2)
            elif op == "C":
                result -= stack.pop()
            else:
                result += int(op)
                stack.append(int(op))

        return sum(stack)
        