class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create array with pairs of position and speed
        pair = [[p, s] for p, s in zip(position, speed)]

        stack = []

        # Iterate through the sorted pair array
        for p, s in sorted(pair)[::-1]:
            # Append the current value to the stack
            stack.append([p, s])

            if len(stack) > 1:
                # Compare distances
                time_top = (target - stack[-1][0]) / (stack[-1][1])
                time_next = (target - stack[-2][0]) / (stack[-2][1])

                # Pop and make into one fleet if the time_top gets to the target quicker than what is in the stack (less time)
                if time_top <= time_next:
                    stack.pop()

        return len(stack)
