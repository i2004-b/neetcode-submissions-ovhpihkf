class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Helper function to reverse string
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        # Adjust k to be modded by the len of the list to avoid extra rotations
        k = k % len(nums)

        # Reverse the whole list first
        reverse(0, len(nums) - 1)
        # Reverse the first part of the list
        reverse(0, k - 1)
        # Reverse the second part of the list
        reverse(k, len(nums) - 1)