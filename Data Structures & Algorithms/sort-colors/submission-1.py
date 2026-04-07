class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Left and right pointers
        left, right = 0, len(nums) - 1

        # Tracks through the array
        i = 0

        # Iterate until i is greater than right
        while i <= right:
            if nums[i] == 0:
                temp = nums[i]
                nums[i] = nums[left]
                nums[left] = temp
                left += 1
            elif nums[i] == 2:
                temp = nums[i]
                nums[i] = nums[right]
                nums[right] = temp
                right -= 1
                i -= 1

            i += 1

