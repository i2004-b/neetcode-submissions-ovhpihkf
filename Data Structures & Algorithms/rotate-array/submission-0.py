class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # Time: O(n)
        # Space: O(n)

        shifted = [0] * len(nums)

        for i in range(len(nums)):
            index = (i + k) % len(nums)
            shifted[index] = nums[i]
            
        print(shifted)
        nums[:] = shifted
        