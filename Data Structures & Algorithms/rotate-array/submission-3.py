class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        shift = k % len(nums)

        arr1 = nums[len(nums) - shift:]
        arr2 = nums[: len(nums) - shift]

        nums[: len(arr1)] = arr1
        nums[len(arr1):] = arr2