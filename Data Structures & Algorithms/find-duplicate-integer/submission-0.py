class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Floyd pointer technique
        # Phase 1: start the slow and fast pointers --> find intersection
        # The item at the 0th index will never repeat as the numbers range from 1 to n
        slow, fast = 0, 0

        # Iterate while true
        while True:
            # Move the slow pointer
            slow = nums[slow]
            # Move the fast pointer twice
            fast = nums[nums[fast]]
            # If both are equal, return break from the loop
            if slow == fast:
                break

        # Phase 2: get another slow pointer --> find duplicate
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

        