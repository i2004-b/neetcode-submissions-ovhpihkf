class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for index, num in enumerate(nums):
            val = target - num
            if val in indices:
                return [indices[val], index]

            indices[num] = index

        return False


