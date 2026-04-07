class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums) // 2

        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

            """
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
            """

        for num in count:
            if count[num] > majority:
                return num