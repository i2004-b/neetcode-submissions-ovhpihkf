class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for op in tokens:
            if op == "+":
                x, y = stack.pop(), stack.pop()
                stack.append(x + y)
            elif op == "-":
                x, y = stack.pop(), stack.pop()
                stack.append(y - x)
            elif op == "*":
                x, y = stack.pop(), stack.pop()
                stack.append(x * y)
            elif op == "/":
                x, y = stack.pop(), stack.pop()
                stack.append(int(y / x))
            else:
                stack.append(int(op))

                
        return stack[-1]