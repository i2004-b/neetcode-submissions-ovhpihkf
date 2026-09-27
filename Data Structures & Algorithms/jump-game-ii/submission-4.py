class Solution:
    def jump(self, nums: List[int]) -> int:
        # Greedy algorithm transforms this into a flat BFS
        """
        Want to traverse through the nums array treating it as different sections
        You need two pointers to demonstrate the boundary
        Set a result variable to 0 (add 1 when you create new level)
        Iterate while the right most boundary is < len(nums) - 1 (once right is in the last boundary, you have a way to reach it)
        Iterate through the items in the window
        Set a farthest length variable that is updates depending on how far you can jump (that index + that number)
        Reassign the pointers: l --> r; r --> farthest
        Update the result

        Return the result
        """

        res = 0
        l, r = 0, 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, nums[i] + i)
            
            l = r + 1
            r = farthest
            res += 1
            
        return res