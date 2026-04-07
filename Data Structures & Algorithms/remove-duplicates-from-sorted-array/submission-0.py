class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1 # Set k equal to one because min length of list is 1

        # Iterate starting at 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k

        