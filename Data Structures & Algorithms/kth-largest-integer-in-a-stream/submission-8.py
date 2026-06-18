class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Declare member variables for the heap and k
        self.minHeap, self.k = nums, k

        # Turn the minHeap into a heap using heapfiy
        heapq.heapify(self.minHeap)

        # Pop elements from the heap if it has more than k elements
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # Add the value to the heap
        heapq.heappush(self.minHeap, val)

        # Pop the value if the heap has more than k elements
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        # Return the 0-index value of the heap
        return self.minHeap[0]
        
