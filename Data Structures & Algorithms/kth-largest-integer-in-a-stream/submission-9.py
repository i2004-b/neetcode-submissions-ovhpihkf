class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # First, declare member variables for the heap and the k
        self.min_heap, self.k = nums, k

        # Heapify the min_heap
        heapq.heapify(self.min_heap)

        # Delete from the heap if it greater than k elements
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        # Add the value regardless
        heapq.heappush(self.min_heap, val)
        # Check that the length is valid
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        # Return the minimum element
        return self.min_heap[0]
         
