class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        for i in range(1, len(nums)):
            output[i] = nums[i - 1] * output[i - 1]
        
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= post
            post *= nums[i]

        return output
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """# Take length of nums
        length = len(nums)

        # Declare 3 arrays: pre, post, and output
        pre = [1] * length
        post = [1] * length
        output = [0] * length

        # Fill the prefix
        for i in range(1, length):
            pre[i] = pre[i - 1] * nums[i - 1]
        
        # Fill the postfix
        for i in range(length - 2, -1, -1):
            post[i] = post[i + 1] * nums[i + 1]
        
        # Fill in the output
        for i in range(length):
            output[i] = pre[i] * post[i]

        return output"""
