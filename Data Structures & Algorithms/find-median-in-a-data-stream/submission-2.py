class MedianFinder:
    """
    Uses a two heap method:
        1) A heap holding values smaller than the other half (that is implemented as a max heap)
        2) A heap holding values larger than the other half (that is implemented as a min heap)
    """

    def __init__(self):
        # Declare two heaps
        self.small_heap = []
        self.large_heap = []
        
    def addNum(self, num: int) -> None:
        # Add number to the correct heap
        # If the large_heap exists and the current number is >= than the top of it, add it there; otherwise, add to the small_heap
        if self.large_heap and num >= self.large_heap[0]:
            heapq.heappush(self.large_heap, num)
        else:
            heapq.heappush(self.small_heap, -num) # Negative to maintain the max heap

        # Check if imbalanced
        if len(self.small_heap) > len(self.large_heap) + 1:
            # Move a value from small to large
            # Negate it again to get rid of negative sign
            val = -heapq.heappop(self.small_heap)
            heapq.heappush(self.large_heap, val)
        elif len(self.large_heap) > len(self.small_heap) + 1:
            # Pop the value
            val = heapq.heappop(self.large_heap)
            # Negate the value to maintain the max_heap
            heapq.heappush(self.small_heap, -val)

    def findMedian(self) -> float:
        # Check if the lengths are not equal, meaning that the total nums passed in were odd
        if len(self.small_heap) > len(self.large_heap):
            return -self.small_heap[0]
        elif len(self.large_heap) > len(self.small_heap):
            return self.large_heap[0]
        # The number of values passed in was even
        else:
            return (-self.small_heap[0] + self.large_heap[0]) / 2
        