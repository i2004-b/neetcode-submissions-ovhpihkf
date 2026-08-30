class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Declare array to hold longest subsequence at that point
        dp = [1] * len(nums)
        # Track the longest increasing subsequence
        lis = 1 

        # Iterate through the nums (except the first one)
        for i in range(1, len(nums)):
            # Iterate through the previous nums
            for j in range(i):
                # Check if current number is greater than number at j
                if nums[i] > nums[j]:
                    # Update dp
                    dp[i] = max(dp[i], dp[j] + 1)
                    # Update result
                    lis = max(lis, dp[i])

        return lis