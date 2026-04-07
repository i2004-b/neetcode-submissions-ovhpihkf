class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        duplicates = {}
        l = 0

        for r in range(len(nums)):
            if r - l > k:
                duplicates[nums[l]] -= 1
                if duplicates[nums[l]] == 0:
                    del duplicates[nums[l]]
                l += 1

            if nums[r] in duplicates:
                return True

            duplicates[nums[r]] = 1

        return False