class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Declare minHeap and k member variables
        self.minHeap, self.k = nums, k
        # Heapify the minHeap
        heapq.heapify(self.minHeap)

        # Pop the smallest value if heap has more than k elements
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # Push the value into the heap
        heapq.heappush(self.minHeap, val)
        # Only pop if the list has more than k elements
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        # Return the kth largest value which will be minimum of our heap
        return self.minHeap[0]