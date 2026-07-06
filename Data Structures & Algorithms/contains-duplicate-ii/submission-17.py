class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Hashmap solution
        duplicates = {}

        l = 0

        for r in range(len(nums)):
            # Delete from the map
            if r - l > k:
                duplicates[nums[l]] -= 1
                if duplicates[nums[l]] == 0:
                    del duplicates[nums[l]]

                # Increment l
                l += 1
        
            # Return true from the map
            if nums[r] in duplicates:
                return True

            # Add value to the map
            duplicates[nums[r]] = 1 + duplicates.get(nums[r], 0)

        return False
