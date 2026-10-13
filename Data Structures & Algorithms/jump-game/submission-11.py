class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        given nums 
        each location represents max length of jump 
        return true if we can reach last index when beginning from inde 0 or we do false

        if we land at last index: return True
        if we land on a 0 --> dead spot: return false
        """
        """
        def dfs(ind):
            if ind == len(nums) - 1:
                return True 

            for step in range(1, nums[ind] + 1):
                if dfs(ind + step):
                    return True

            return False

        return dfs(0)
        """

        """
        Bascially check if we can get to the end from the second to last place; if so, move the marker

        iterate backwards through the list 
        have a pointer to the end (goal)
        goal will only move if that spot can be gotten to
        """

        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            # Check the value in that index spot
            if i + nums[i] >= goal:
                goal = i
        
        return goal == 0