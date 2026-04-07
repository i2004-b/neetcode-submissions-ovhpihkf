class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        longest_sub = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    longest_sub[i] = max(longest_sub[i], 1 + longest_sub[j])

        return max(longest_sub)