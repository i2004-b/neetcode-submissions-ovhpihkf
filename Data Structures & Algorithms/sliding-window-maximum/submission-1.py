class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Solution #1: Use a heap to track the main element
        What to do:
            Declare a heap
            Declare an output list
            Iterate through the list of nums
                Add the newly encountered value to the heap (add the (-) value and the index)
                Check if the window size has been reached:
                    If the window size has been reached, iterate while the top of the heap is not in range
                        Pop the max_values as long as they are not in range
                    Append to the output list the value (make sure to negate again to ensure no negatives end up in list)
            Return the output list  
        
        Complexity:
        T: O(nlogn)
        S: O(n)
        """

        # Declare the heap and the output DS
        heap = []
        output = []

        # Iterate through the numbers array
        for r in range(len(nums)):
            # Add the value and its index to the heap
            heapq.heappush(heap, (-nums[r], r)) # Second value is the index (needed to check window size)

            # Check if window size has been met
            if r + 1 >= k:
                # Remove any values that are not within the window
                while heap[0][1] <= r - k:
                    heapq.heappop(heap)
                # Add the highest value to the output list
                output.append(-heap[0][0])

        return output