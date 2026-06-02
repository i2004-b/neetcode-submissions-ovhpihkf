class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Insertion Sort Implementation

        # Outer loop iterates from index 1 onwards because index 0 is sorted (when on its own)
        for i in range(1, len(nums)):
            # Initialize pointer to go through the elements before i
            j = i - 1
            # Iterate while j in bounds and the previous value is greater than the current value
            while j >= 0 and nums[j] > nums[j + 1]:
                # Swap the values
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                # Decrement j
                j -= 1

        # Return list
        return nums