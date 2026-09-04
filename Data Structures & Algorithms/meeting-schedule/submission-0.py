"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Sort the array based on the start value
        intervals.sort(key=lambda x:x.start)

        # Iterate through the values from 1 to the end
        for i in range(1, len(intervals)):
            # Save where the previous item ended
            prev_end = intervals[i - 1].end
            # Save where the current item begins
            curr_start = intervals[i].start

            # If curr_start comes before the previous ends, return false
            if curr_start < prev_end:
                return False

        # Return True, as exiting the loop means there were no conflicts
        return True       