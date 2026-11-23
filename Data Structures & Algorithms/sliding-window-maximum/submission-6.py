class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Attempt at the queue Solution
        # Declare a queue
        queue = deque()
        # Declare output List
        output = []

        # Declare left pointer
        l = 0

        # Iterate through the List
        for r in range(len(nums)):
            # Check if queue exists and the current value at r is greater than the value at the end of the queue, pop from the queue
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()

            # Add the current index
            queue.append(r)

            # Check if top is less than l
            if queue[0] < l:
                queue.popleft()

            # If it is the correct length
            if r - l + 1 == k:
                output.append(nums[queue[0]])
                l += 1


        return output