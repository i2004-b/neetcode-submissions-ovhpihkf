class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create array of pairs of position and speed
        pairs = [[p, s] for p, s in zip(position, speed)]
        # Sort the pairs in reverse order
        pairs.sort(reverse=True)

        # Declare a stack
        stack = []

        # Iterate through the array that has been reversed
        for p, s in pairs:
            # Append the new time to the stack
            stack.append((target - p) / s)

            # Quicker time means that the car will reach the end quicker
            # If it is quicker than or the same as the prev car, they collide to make one fleet
            # Ensure stack exists also
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                # Pop from the stack
                stack.pop()

        # Return the length of the stack
        return len(stack)
