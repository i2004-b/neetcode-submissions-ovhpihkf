class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        l = 0

        for r in range(len(nums)):
            if r - l > k:
                # Delete value at left pointer and increment l to get back to k window
                window.remove(nums[l])
                l += 1

            # If new value seen, return true
            if nums[r] in window:
                return True

            # Add the value to the set otherwise
            window.add(nums[r])

        return False