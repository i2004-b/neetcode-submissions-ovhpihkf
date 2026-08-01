class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Create a heap for the stones stones
        max_heap = []
        # Need to simulate a max heap using negative signs so iterate through stones
        for stone in stones:
            heapq.heappush(max_heap, -stone)

        while len(max_heap) > 1:
            x, y = -heapq.heappop(max_heap), -heapq.heappop(max_heap)
            if x < y:
                heapq.heappush(max_heap, -(y - x))
            elif y < x:
                heapq.heappush(max_heap, -(x - y))

        return -max_heap[0] if max_heap else 0
        