class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Sorted in non-decreasing order
        # Remove duplicates so that each appears once
        # if number before is the same, keep pointer there because you want to replace it
        # if not the same, put it there

        k = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[k] = nums[i]
                k += 1

        return k