class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Declare two pointers to point to the ends of the array
        l, r = 0, len(nums) - 1

        # Iterate through the list while l <= r
        while l <= r:
            # Calculate mid
            mid = (l + r) // 2

            # If you encounter the correct number, return
            if nums[mid] == target:
                return mid

            # Break the problem into sublists
            # Left sublist
            if nums[l] <= nums[mid]:
                # Move the pointer left in two cases: target is greater than mid or target is less than nums[l]
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # Right sublist
            else:
                # Move the pointer to the right in two cases: target is less than mid or target is greater than nums[r]
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return -1