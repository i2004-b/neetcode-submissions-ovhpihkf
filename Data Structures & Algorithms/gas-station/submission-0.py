class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Check if it is possible by comparing the sums of both lists
        if sum(cost) > sum(gas):
            return -1

        # If above condition is False, a solution will exist

        # Set a tracker and a res variable
        tracker = 0
        res = 0 # Index of where to start from

        # Iterate through the length of the lists
        for i in range(len(gas)):
            # Update tracker to the difference between gas and cost
            tracker += gas[i] - cost[i]
            # If tracker ever falls below 0, that starting point is not valid
            if tracker < 0:
                tracker = 0
                res = i + 1

        return res
            