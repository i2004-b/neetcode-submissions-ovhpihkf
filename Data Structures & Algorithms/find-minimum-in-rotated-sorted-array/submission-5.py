class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        # For this method, the min value will be where l is at
        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        
        return nums[l]
            