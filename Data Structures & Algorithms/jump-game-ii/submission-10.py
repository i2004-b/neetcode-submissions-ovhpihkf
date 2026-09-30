class Solution:
    def jump(self, nums: List[int]) -> int:
        # Greedy Solution
        # Count the number of steps
        count = 0
        # Have pointers
        i, j = 0, 0

        # Iterate while j is in bounds
        while j < len(nums) - 1:
            furthest = 0

            for k in range(i, j + 1):
                furthest = max(furthest, nums[k] + k) # Key is max is not just the maximum + j; if it the maximum from that point because that point is the only one that can add that number to that point

            i = j + 1
            j = furthest
            count += 1

        return count
