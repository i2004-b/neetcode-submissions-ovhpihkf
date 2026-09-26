class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Declare two pointers (curr and dest)
        curr, dest = len(nums) - 2, len(nums) - 1

        # Iterate while curr is greater than or equal to 0
        while curr >= 0:
            # Check if the distance between dest and curr can be made by a number in the range of (0, nums[i])
            if dest - curr <= nums[curr]:
                # Move both pointers
                dest = curr
            curr -= 1

        return True if dest == 0 else False

