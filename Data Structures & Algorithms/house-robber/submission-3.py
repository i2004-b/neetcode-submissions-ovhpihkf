class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        money = [0] * len(nums)

        # Base cases
        money[0] = nums[0]
        
        if nums[0] > nums[1]:
            money[1] = nums[0]
        else:
            money[1] = nums[1]
        

        for i in range(2, len(nums)):
            money[i] = max(nums[i] + money[i - 2], money[i - 1])

        return money[-1]