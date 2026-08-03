class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # First, create a dictionary with the counts for each element in tasks
        count = {}

        for task in tasks:
            count[task] = 1 + count.get(task, 0)

        # Add values to the max_heap before heapifying
        # Using a max heap to figure out what values are most frequent
        max_heap = [-cnt for cnt in count.values()]
        # Heapify
        heapq.heapify(max_heap)

        # Initialize the time to be 0
        time = 0
        # Initialize a queue that will hold items as pairs -> [-cnt, time + n]
        queue = deque()

        # Iterate while either the heap or the queue exists
        while max_heap or queue:
            # Increment the time by 1
            time += 1

            # Check if the heap exists
            if max_heap:
                # Get the count
                # Add 1 to the count to update the value (decrementing it because the value is negative)
                cnt = heapq.heappop(max_heap) + 1
                # If the cnt is non-zero, add to the queue
                if cnt:
                    queue.append([cnt, time + n])
            
            # Check that the queue exists and that the time of the first element has been reached
            if queue and queue[0][1] == time:
                # Pop from the queue and add into the heap just the value of cnt
                heapq.heappush(max_heap, queue.popleft()[0])

        return time