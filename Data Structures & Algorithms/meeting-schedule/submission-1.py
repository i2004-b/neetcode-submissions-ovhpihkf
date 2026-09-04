"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        """
        Solution Description:
        Looking to see if the meetings overlap. The easiest way to do this is the following:
            1) Sort the array based on the start values (get chronological order of meetings)
            2) Check for overlap
                - Because array is sorted, simply check if one meeting starts before the previous one ended. If this is the case return False
            3) Return True if you successfully went through the loop

        Time: O(nlogn) (driven by sorting algorithm)
        Space: O(1) or O(n) (depends on the sorting algorithm)
        """

        # Sort the elements by the start value
        # Each item in the list of intervals is an object; access its starting item
        intervals.sort(key = lambda x:x.start)

        # Iterate through the items
        for i in range(1, len(intervals)):
            # Find when current interval starts
            curr_start = intervals[i].start
            # Find when prev interval ends
            prev_end = intervals[i - 1].end

            # If meeting starts before previous ends, return False
            if curr_start < prev_end:
                return False
                
        return True