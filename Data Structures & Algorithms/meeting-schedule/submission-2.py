"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # For interval questions, good to put them in order for easier comparison
        # The intervals are not lists or tuples but rather objects so approach with care

        # First sort the list based on the objects
        # Key has to be assigned to a function
        intervals.sort(key=lambda x: x.start)

        # You can make all the meetings if the begin time time is >= the prev end time
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                return False

        return True
