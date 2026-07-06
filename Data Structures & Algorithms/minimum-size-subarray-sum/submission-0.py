class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Track the length 
        length = float("inf")
        # Set the current sum and the left pointer to 0
        curr_sum, l = 0, 0

        # Iterate through the whole array with the "right" pointer
        for r in range(len(nums)):
            # Add to the curr_sum
            curr_sum += nums[r]

            # Update left while the curr_sum >= target
            while curr_sum >= target:
                # Update length
                length = min(length, r - l + 1)
                # Deduct value where left is from curr_sum
                curr_sum -= nums[l]
                # Increment l
                l += 1

        # Return length is not infinity, else, return 0
        return length if length != float("inf") else 0


