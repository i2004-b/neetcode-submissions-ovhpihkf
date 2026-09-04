"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Alternative way of writing the two pointers Solution
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        # Set result, cnt, and pointers
        res, cnt, s, e = 0, 0, 0, 0

        # Iterate while s is in bounds
        while s < len(start):
            # If the start value is less than the end value, a new meeting began; increase cnt and increment pointer
            if start[s] < end[e]:
                cnt += 1
                s += 1
            else:
                cnt -= 1
                e += 1

            # Update result
            res = max(res, cnt)

        return res