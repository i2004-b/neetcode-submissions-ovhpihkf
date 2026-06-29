class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Track the maxArea using a variable
        maxArea = 0
        # Initialize a stack that will hold pairs: (index, height)
        stack = []

        # Iterate through heights, getting the index and the heights
        for i, h in enumerate(heights):
            # Set the start index to the current index i
            start = i
            # Iterate while the stack exists and the value before is greater
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                # Update the maxArea
                maxArea = max(maxArea, height * (i - index))
                # Update start
                start = index
                """
                # Calculate the maxArea
                maxArea = max(maxArea, stack[-1][1] * (i - stack[-1][0]))
                # Update the start value
                start = stack[-1][0]
                # Pop item from the stack
                stack.pop()
                """
            # Append the current value to the stack
            stack.append((start, h))

        # Iterate through values that are still present in the stack
        for i, h in stack:
            # Calculate the max height for them and update if needed
            # The remaining values go through the end of the list, so use the length of heights as right boundary
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea