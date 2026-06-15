class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        pre = [1] * len(nums)
        post = [1] * len(nums)

        for i in range(1, len(nums)):
            pre[i] = nums[i - 1] * pre[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            post[i] = nums[i + 1] * post[i + 1]

        for i in range(len(output)):
            output[i] = pre[i] * post[i]

        return output














































        """
        # Get length of nums
        length = len(nums)
        # Declare output array initialized with 1s
        output = [1] * length

        # Set prefix and postfix equal to 1 initially
        prefix, postfix = 1, 1

        # Iterate through output array and save the prefix sums
        for i in range(length):
            output[i] = prefix
            # Update prefix
            prefix *= nums[i]

        # Iterate through output array from behind to get product without value
        for i in range(length - 1, -1, -1):
            output[i] *= postfix
            # Update post
            postfix *= nums[i]

        # Return output
        return output
        """