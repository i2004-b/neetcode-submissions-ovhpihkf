class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count dictionary to hold the counts for each letter
        count = {}

        # Fill the dictionary with all the appropriate counts
        for task in tasks:
            count[task] = 1 + count.get(task, 0)

        # Declare a max_heap and initially fill it with the negative count values
        max_heap = [-cnt for cnt in count.values()]
        # Heapify
        heapq.heapify(max_heap)

        # Declare queue to keep track of item that needs to be added into the heap
        queue = deque()

        # Track the time
        time = 0

        # Iterate while the heap or queue exists
        while max_heap or queue:
            # Update the time
            time += 1

            # Check if the heap exists
            if max_heap:
                # Update the count
                count = heapq.heappop(max_heap) + 1
                # If the count is not zero, add it, with the time it should reappear, into queue
                if count:
                    queue.append([count, time + n])

            # Check that the queue exists and that it is time for the front value to come back in
            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])

        return time