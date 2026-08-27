class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track = {}

        for ind, num in enumerate(nums):
            sol = target - num
            if sol in track:
                return [track[sol], ind]
            
            track[num] = ind

        