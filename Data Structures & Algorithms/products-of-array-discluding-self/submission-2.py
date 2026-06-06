class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Declare arrays, initialized with 1s, to store pre and post sums
        pre = [1] * len(nums)
        post = [1] * len(nums)

        # Iterate through pre and put product of values before it into the spot
        # If the first element, just do 1 * the element
        for i in range(len(nums)):
            if i == 0:
                pre[i] *= nums[i]
            else:
                pre[i] = pre[i - 1] * nums[i]

        # Iterate backwards through post and put product of values after it into the spot
        # For the last element, just do 1 * the value
        for j in range(len(nums) - 1, -1, -1):
            if j == len(nums) - 1:
                post[j] *= nums[j]
            else:
                post[j] = post[j + 1] * nums[j]

        # Declare output array
        output = []

        # Iterate through and put vals in by adding the value before and after in 
        # Edge cases: first value (only add from post) and last value (only add from pre)
        for k in range(len(nums)):
            if k == 0:
                output.append(post[1])
            elif k == len(nums) - 1:
                output.append(pre[-2])
            else:
                output.append(pre[k - 1] * post[k + 1])
        
        return output