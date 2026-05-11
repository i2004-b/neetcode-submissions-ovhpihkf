class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = set()

        for num in nums:
            # Return True if the number was already seen
            if num in dup:
                return True
            
            # Add the current number to the set
            dup.add(num)

        # Return False if there were no duplicates
        return False