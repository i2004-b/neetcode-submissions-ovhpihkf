class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            # Check that the current portion is already sorted
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            # Find middle 
            mid = (l + r) // 2
            # Update result
            res = min(res, nums[mid])

            # If the number at the middle point is greater than or equal to the leftmost value, move right
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        return res