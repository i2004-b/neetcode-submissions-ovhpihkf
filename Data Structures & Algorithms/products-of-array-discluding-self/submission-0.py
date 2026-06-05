class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Declare output array to keep track of outputs
        output = [0] * len(nums)
        total_product = 1
        zero_count = 0

        for num in nums:
            if num != 0:
                total_product *= num
            else:
                zero_count += 1
        
        for i in range(len(nums)):
            if not zero_count:
                output[i] = total_product // nums[i]
            elif zero_count == 1 and nums[i] == 0:
                output[i] = total_product

        return output
