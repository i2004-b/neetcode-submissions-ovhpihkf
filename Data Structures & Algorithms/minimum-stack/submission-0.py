class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack and self.stack[-1][1] < val:
            self.stack.append((val, self.stack[-1][1]))
        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        val, min_val = self.stack.pop()
        return val
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        
