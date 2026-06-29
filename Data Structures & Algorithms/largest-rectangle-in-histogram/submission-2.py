class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Length of heights array
        n = len(heights)
        # Hold the maxArea
        maxArea = 0
        # Empty stack to hold indices
        stack = []

        # Iterate through the length of heights + 1
        for i in range(n + 1):
            while stack and (i == n or heights[i] <= heights[stack[-1]]):
                # Pop the top index and get height
                h = heights[stack.pop()]
                # Compute the width
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                maxArea = max(maxArea, h * width)
            stack.append(i)

        return maxArea