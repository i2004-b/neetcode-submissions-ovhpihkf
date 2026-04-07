class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # Time: O(n)
        # Space: O(n)
        # Declare stack
        stack = []

        # Iterate through operations
        for op in operations:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                stack.append(stack[-1] * 2)
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))

        return sum(stack)
        