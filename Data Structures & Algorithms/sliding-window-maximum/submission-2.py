class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Solution #2: Use a deque (monotonically decreasing deque)

        Strategy: Add and pop items from a queue (both operations are constant time and when doing this over a list, it is O(n))

        What to Do:
            Declare an output array and a queue
            Set pointers (definitely need to set left; can set r also if you are using a while loop)
            Iterate until the end of the list:
                If the queue exists and the value there is less than the value you want to add, you need to remove these values
                (as the new value will be greater than them so in any case of a max, the new value will be used)
                Once you finish removing smaller elements, add the new element to the queue (adding the indices of values to the queue)

                Pop the leftmost item if the index is less than the leftmost pointer

                Check if a proper window size has been reached:
                    If so, add the max to the output array
                    Increment the left pointer

                If you also have a right pointer, increment the right pointer

            Return the output array

        Complexity:
        Time: O(n)
        Space: O(n)
        """
        
        # Declare output array and the queue
        output = []
        queue = deque()

        # Declare the left pointer
        l = 0

        # Iterate through the list
        for r in range(len(nums)):
            # Before adding the value to the queue, remove from the right end any values that are smaller than it
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            
            # Add the new value to the queue (just add index)
            queue.append(r)

            # Pop the front-most element in the case that it is out of bounds of the window
            if l > queue[0]:
                queue.popleft()

            # If the window size has been achieved, add the max to the output
            if r + 1 >= k:
                # Add the actual value, not just the index
                output.append(nums[queue[0]])
                # Increment the left pointer
                l += 1

        return output