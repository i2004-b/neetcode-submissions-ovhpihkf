class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Heap Solution Retry (store the max (negated) at the top point of the heap)

        heap = []
        output = []

        for r in range(len(nums)):
            # Add the new value to the top of the heap
            heapq.heappush(heap, (-nums[r], r)) # Push in the value (negated) and the index
            # Check if a proper window size has been reached
            if r + 1 >= k:
                # Remove top values if they are outside of the window
                while heap[0][1] <= r - k:
                    heapq.heappop(heap)
                # Add the max value for the window to the output array
                output.append(-heap[0][0])

        # return the output list
        return output
