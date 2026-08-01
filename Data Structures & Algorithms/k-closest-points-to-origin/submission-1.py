class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        res = []

        for coord in points:
            x, y = coord
            distance = -(x**2 + y**2)
            heapq.heappush(max_heap, [distance, x, y])
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        while max_heap:
            dist, x, y = heapq.heappop(max_heap)
            res.append([x, y])

        return res