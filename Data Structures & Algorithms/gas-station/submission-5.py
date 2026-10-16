class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Two pointers technique: O(n) time and O(1) space 
        # Length of the arrays
        length = len(gas)

        # Set pointers to the start and end of the circle
        start, end = length - 1, 0

        # Get the tank amount currently
        tank = gas[start] - cost[start]

        # Iterate while start is greater than end
        while start > end:
            # Check if the tank is negative
            # In this case, you would have to move the start over
            if tank < 0:
                start -= 1
                tank += (gas[start] - cost[start])
            # If the tank is >= 0, then keep adding from the end
            else:
                tank += (gas[end] - cost[end])
                end += 1

        return start if tank >= 0 else -1
