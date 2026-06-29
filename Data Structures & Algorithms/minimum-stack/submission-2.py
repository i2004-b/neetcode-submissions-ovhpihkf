class MinStack:

    def __init__(self):
        # Set minimum to an infinite value
        self.min = float("inf")
        # Declare stack
        self.stack = []

    def push(self, val: int) -> None:
        # If the stack does not exist, assign the val to min and push 0 to stack
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            # Append to the stack the value minus the minimum value
            self.stack.append(val - self.min)
            # Reset the minimum if the value is less than the current minimum
            if val < self.min:
                self.min = val
        

    def pop(self) -> None:
        # If the stack does not exist, return nothing
        if not self.stack:
            return

        # Pop the value in the stack
        popped = self.stack.pop()

        # If popped is negative, need to update the minimum
        if popped < 0:
            self.min = self.min - popped


    def top(self) -> int:
        # Get the top value from the stack
        top = self.stack[-1]

        if top > 0:
            return top + self.min
        else:
            return self.min


    def getMin(self) -> int:
        return self.min
        
