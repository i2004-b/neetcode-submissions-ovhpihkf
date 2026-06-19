class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1

        max_heap = stones

        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            x, y = -(heapq.heappop(max_heap)), -(heapq.heappop(max_heap))

            if x < y:
                y -= x
                heapq.heappush(max_heap, -y)
            elif x > y:
                x -= y
                heapq.heappush(max_heap, -x)

        return -(max_heap[0]) if max_heap else 0