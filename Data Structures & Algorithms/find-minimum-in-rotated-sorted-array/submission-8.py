class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Declare pointers to the ends of the array
        l, r = 0, len(nums) - 1
        # Set result just to the number at the last spot
        res = nums[r]

        if nums[l] < nums[r]:
            return nums[l]

        while l <= r:
            # Calculate the middle
            mid = (l + r) // 2

            # Update the result if needed
            res = min(res, nums[mid])

            # Update the pointers
            
            if nums[r] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return res