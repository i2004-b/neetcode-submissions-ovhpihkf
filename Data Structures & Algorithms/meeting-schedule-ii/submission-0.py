"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Declare two arrays; one will hold start and the other end values
        start = []
        end = []

        # Iterate through interval and add appropriate values to previous lists
        for meet in intervals:
            start.append(meet.start)
            end.append(meet.end)

        # Sort both
        start.sort()
        end.sort()

        # Declare two pointers to traverse the array
        i, j = 0, 0

        # Declare result and count variables
        res, cnt = 0, 0

        # Iterate while the start array still has items
        while i < len(start):
            if start[i] < end[j]:
                # Update cnt and i
                cnt += 1
                i += 1
            else:
                cnt -= 1
                j += 1

            # Update result
            res = max(res, cnt)

        return res