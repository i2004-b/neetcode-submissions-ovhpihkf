class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Monotonically Decreasing Deque retry
        # Declare a queue and an output list
        queue = deque() # Will store indices (with the leftmost index being where the max for the window is)
        output = []

        # Declare a left pointer
        l = 0

        # Iterate through the list
        for r in range(len(nums)):
            # First check if the value that is being added is greater than the rightmost value
            # While the queue exists and the above is true, delete from the right
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()

            # Add the new value to the queue
            queue.append(r)

            # Pop the leftmost value in the case that it is outside the window range
            if l > queue[0]:
                queue.popleft()

            # Check that the window size has been reached before inputting into the output array
            if r + 1 >= k:
                output.append(nums[queue[0]])
                # Update the left pointer only if the window size has been reached
                l += 1

        return output