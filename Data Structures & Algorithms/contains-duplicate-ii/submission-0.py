class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Need set to keep track of duplicates
        window = set()
        # Intialize left pointer
        L = 0

        # Iterate through the array
        for R in range(len(nums)):
            # Update left pointer only if the indices are outside the restricted bound
            # Remove the former left element from the list as well
            if R - L > k:
                window.remove(nums[L])
                L += 1
            # Return True if the item was already in the list, indicating duplicate
            if nums[R] in window:
                return True
            # Add to the set otherwise
            window.add(nums[R])

        # If the duplicate is not found, conditions are not met, so return False
        return False