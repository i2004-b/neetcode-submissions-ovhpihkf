class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        appearances = {}

        for item in nums:
            if item not in appearances:
                appearances[item] = 1
            else:
                appearances[item] += 1
        
        for key in appearances:
            if appearances[key] > 1:
                return True
        
        return False