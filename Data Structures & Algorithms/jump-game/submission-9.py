class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dest = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if dest - i <= nums[i]:
                dest = i
        
        return True if dest == 0 else False