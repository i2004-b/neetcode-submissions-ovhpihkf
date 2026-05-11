class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = {}

        for num in nums:
            # Add to the count
            dup[num] = 1 + dup.get(num, 0)
            
            # Return True if there was a duplicate
            if dup[num] > 1:
                return True

        return False