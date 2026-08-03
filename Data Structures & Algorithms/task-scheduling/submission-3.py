class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Slight optimization in that you update the time to be the value at the first element in the queue if heap does not exist
        count = {}

        for task in tasks:
            count[task] = 1 + count.get(task, 0)

        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)

        time = 0
        queue = deque()

        while max_heap or queue:
            time += 1

            if not max_heap:
                time = queue[0][1]
            else:
                # Get the count
                cnt = heapq.heappop(max_heap) + 1
                # If cnt is non-zero, add to queue
                if cnt:
                    queue.append([cnt, time + n])

            # Check that the queue exists and the value at the beginning of the queue is the current time
            if queue and queue[0][1] == time:
                # Add to the max_heap
                heapq.heappush(max_heap, queue.popleft()[0])

        return time