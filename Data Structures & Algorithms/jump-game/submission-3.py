class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Create array that holds if yoou can get to the end from that value
        dp = [False] * len(nums)
        # Set last element to True
        dp[-1] = True

        # Iterate from the second to last element
        for i in range(len(nums) - 2, -1, -1):
            # Go through numbers
            # for j in range(i + 1, min(i + nums[i] + 1, len(nums) - 1)):
            #     if dp[j]:
            #         dp[i] = True
            #         break

            for j in range(1, nums[i] + 1):
                if j >= len(nums):
                    break
                
                if dp[i + j]:
                    dp[i] = True
                    break


        return dp[0]