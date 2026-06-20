class Solution:
    def trap(self, height: List[int]) -> int:
        # T: O(n), S: O(1)
        # Check if the height array is empty
        if not height:
            return 0

        # Declare left and right pointers
        l, r = 0, len(height) - 1
        # Declare maximum on each side
        leftMax, rightMax = height[l], height[r]
        # Result variable to keep track of result
        res = 0

        # Iterate while left is less than right
        while l < r:
            # Compare the max values on each side
            if leftMax < rightMax:
                # Move the left pointer
                l += 1
                # Update the leftMax
                leftMax = max(leftMax, height[l])
                # Update result
                res += leftMax - height[l]
            else:
                # Update the right pointer
                r -= 1
                # Update the rightMax
                rightMax = max(rightMax, height[r])
                # Update the result
                res += rightMax - height[r]

        # Return the result
        return res
