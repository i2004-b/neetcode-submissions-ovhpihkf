class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        # Declare helper function
        def robber(i, j): # Pass in indices
            rob1, rob2 = 0, 0

            for x in range(i, j + 1):
                rob1, rob2 = rob2, max(rob2, nums[x] + rob1)

            return rob2

        return max(robber(0, len(nums) - 2), robber(1, len(nums) - 1))
