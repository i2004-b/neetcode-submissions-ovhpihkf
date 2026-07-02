class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        min_val = float("inf")

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] <= nums[r]:
                min_val = min(min_val, nums[mid])
                r = mid - 1
            elif nums[mid] >= nums[l]:
                l = mid + 1
        
        return min_val
        