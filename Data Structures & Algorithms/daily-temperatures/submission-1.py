class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Declare the stack to hold indices of temperatures
        stack = []
        # Declare a pre-filled array that will hold how many days until warmer temperature
        days = [0] * len(temperatures)

        # Iterate through temperatures
        for i in range(len(temperatures)):
            # Iterate while the stack exists and the val at the index at the top of the stack is less than the current value
            while stack and temperatures[stack[-1]] < temperatures[i]:
                # Update the days array
                days[stack[-1]] = i - stack[-1]
                # Pop from stack
                stack.pop()

            # Append current value to the stack
            stack.append(i)

        # Return days
        return days