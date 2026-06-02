class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Set majority element
        majority = nums[0]
        # Keep track of count
        cnt = 1

        # Iterate through remaining elements in list
        for i in range(1, len(nums)):
            # If majority element seen, increment majority by 1
            if nums[i] == majority:
                cnt += 1
            else:
                # Decrement if majority element not seen
                cnt -= 1
                # Reset the majority
                if cnt == 0:
                    majority = nums[i]
                    cnt = 1

        # Return result
        return majority