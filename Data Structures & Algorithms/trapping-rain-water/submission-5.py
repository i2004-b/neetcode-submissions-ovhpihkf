class Solution:
    def trap(self, height: List[int]) -> int:
        # T: O(n), S: O(n)

        """
        This solution tracks the max heights of both the left and the right.
        It then uses the minimum height and then subtracts from that the value in height.
        """

        # Return if height does not exist
        if not height:
            return 0

        length = len(height)
        # Create arrays for the left and right max heights
        leftMax = [0] * length
        rightMax = [0] * length

        # Initial maxes are at the ends of the array
        leftMax[0] = height[0]
        rightMax[-1] = height[-1]

        # Iterate through the leftMax and height array and update the max height
        for i in range(1, length):
            leftMax[i] = max(leftMax[i - 1], height[i])

        # Iterate through the rightMax and height array and update the max height
        for i in range(length - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        # Declare variable to hold the result
        res = 0
        for i in range(length):
            res += min(leftMax[i], rightMax[i]) - height[i]

        return res