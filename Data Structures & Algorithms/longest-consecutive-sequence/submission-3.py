class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Set counter of the longest consecutive sequence
        # Start at zero in case nums is empty
        longest = 0

        # Make a set with all numbers in nums
        seen = set(nums)

        # Iterate through nums
        for num in nums:
            # Sequence counter
            seq = 1
            val = num
            while val + 1 in seen:
                seq += 1
                val += 1

            longest = max(longest, seq)

        return longest

        
