class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Make counts array
        counts = [0] * 3

        # Iterate through the original array and update the count
        for i in range(len(nums)):
            counts[nums[i]] += 1

        # Make pointer to inform about the place to input value
        pntr = 0

        # Iterate through the values in count and add to the original array
        for j in range(len(counts)):
            for _ in range(counts[j]):
                nums[pntr] = j
                pntr += 1
        