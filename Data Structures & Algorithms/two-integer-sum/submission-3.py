class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_and_index = {}

        for index, num in enumerate(nums):
            value = target - num

            if value in val_and_index:
                return [val_and_index[value], index]
            else:
                val_and_index[num] = index