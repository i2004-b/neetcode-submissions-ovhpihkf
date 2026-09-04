"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Min Heap Solution

        # Sort the values in the intervals array based on the start values
        intervals.sort(key=lambda x:x.start)

        # Create a min_heap, initialized with the first meeting end time
        min_heap = []

        # max_len = 1
        # Iterate through the intervals
        for i in range(len(intervals)):
            # Compare the beginning with the top of the heap
            # If it is greater, pop from the heap
            if min_heap and intervals[i].start >= min_heap[0]:
                heapq.heappop(min_heap)
            
            heapq.heappush(min_heap, intervals[i].end)

        return len(min_heap)
