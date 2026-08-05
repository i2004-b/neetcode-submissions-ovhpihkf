class MedianFinder:

    def __init__(self):
        # Initialize two heaps, a max_heap for the smaller values and a min_heap for the larger values
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        # Initially add values to the smaller heap
        heapq.heappush(self.small, -num)

        # Check if the value was put into the correct heap
        # If the top of the small heap is larger, move over to the large heap
        if (self.small and self.large) and (-self.small[0] > self.large[0]):
            # Pop value
            value = -heapq.heappop(self.small)
            # Add value
            heapq.heappush(self.large, value)

        # Check the lengths
        if len(self.small) > len(self.large) + 1:
            # Move from small to the large
            value = -heapq.heappop(self.small)
            heapq.heappush(self.large, value)
        elif len(self.large) > len(self.small) + 1:
            # Move from teh large to the small
            value = heapq.heappop(self.large)
            # Push in negative value
            heapq.heappush(self.small, -value)

    def findMedian(self) -> float:
        # Check to see if the total stream of numbers was odd
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-self.small[0] + self.large[0]) / 2
        
        