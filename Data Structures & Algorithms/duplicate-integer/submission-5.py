class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = Counter(nums)

        for value in duplicates.values():
            if value > 1:
                return True

        return False