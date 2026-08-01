class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Create member variables for the heap and the value k
        self.min_heap, self.k = nums, k

        # Heapify the heap
        heapq.heapify(self.min_heap)

        # Check that the heap only contains k elements
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        # Initially, just add the value to the heap
        heapq.heappush(self.min_heap, val)

        # Check that the length has not exceeded self.k
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        # Return the minimum value: at the first index of the heap
        return self.min_heap[0]
        
