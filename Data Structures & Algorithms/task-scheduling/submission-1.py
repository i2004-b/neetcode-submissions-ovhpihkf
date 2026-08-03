class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        This solution involves a dictionary, max_heap, and queue
        A max_heap is needed to ensure that the most frequent element is accessed (this is used to decrease idle time and complete the task in the minimum amount of time).
        The queue will hold value counts and what time they will next be available.

        Note: for this solution, besides in the dictionary, we do not track the letters as they themselves do not matter much. What matters is the frequency counts.
        The time complexity comes from iterating over the values, m, in tasks.
            Although using a heap, because there are only 26 possible items that can be pushed, the push and pop go from logn to log26, which is a constant.
        The space complexity, similarly, becomes constant as in the dictionary only holds up to 26 different keys, the heap only holds up to 26 different keys, and the queue only holds up to 26 different keys.

        The idle time, because it stays in a constant range does not affect the time complexity. However, if there was no range put on the idle time, the time complexity would evolve to be O(m * n), m being the number of tasks and n being the idle time between the same items being repeated.
        """

        # Count the occurrences of each task and add them to a dictionary
        count = {}

        for task in tasks:
            count[task] = 1 + count.get(task, 0)

        # Declare a max_heap
        max_heap = [-cnt for cnt in count.values()]
        # Heapify
        heapq.heapify(max_heap)

        # Initialize variable to track time.
        time = 0
        # Initialize the queue that will hold pairs --> [-cnt, time + n]
        queue = deque()

        # Iterate while the heap or the queue exists
        while max_heap or queue:
            # Increment the time
            time += 1

            # If the heap exists
            if max_heap:
                # Get the count by popping from the top; update the count by adding 1 (lessening the value)
                cnt = heapq.heappop(max_heap) + 1
                # Add the cnt to the queue if it is greater than 0; add the time when it can be added back as well
                if cnt:
                    queue.append([cnt, time + n])
            
            # Check that the queue exists and the value currently at the front can be added in
            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])

        return time