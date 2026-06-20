class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # T: O(n), S: O(n)

        # Keep track of score
        score = 0
        # Stack to hold previous scores
        stack = []

        # Iterate through operations
        for op in operations:
            if op == "+":
                x, y = stack.pop(), stack[-1]
                stack.append(x)
                stack.append(x + y)
                score += stack[-1]
            elif op == "D":
                stack.append(2 * stack[-1])
                score += stack[-1]
            elif op == "C":
                score -= stack[-1]
                stack.pop()
            else:
                # Turn the integer string into an integer before adding to stack
                stack.append(int(op))
                score += stack[-1]

        return score

        