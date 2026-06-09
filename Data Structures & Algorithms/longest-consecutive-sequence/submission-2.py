class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Longest length
        length = 0

        # Create set with the items in the list
        values = set(nums)

        # Iterate through the array
        for num in nums:
            val = num
            if val - 1 not in values:
                cnt = 1
                while val + 1 in values:
                    cnt += 1
                    val += 1
                length = max(length, cnt)

        return length


        