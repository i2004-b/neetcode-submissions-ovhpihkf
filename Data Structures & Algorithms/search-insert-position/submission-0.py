class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        insert = 0

        while l <= r:
            mid = (r + l) // 2

            if target > nums[mid]:
                l = mid + 1
                insert = l
            elif target < nums[mid]:
                r = mid - 1
                insert = r + 1
            else:
                return mid

        return insert