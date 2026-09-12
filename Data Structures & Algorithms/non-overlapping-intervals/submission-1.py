class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort intervals based on the initial values
        intervals.sort(key = lambda x: x[0])

        # Set result variable to track
        res = 0

        # Set the end value to that of the inital interval
        end = intervals[0][1]

        # Iterate through the rest of the intervals
        for i in range(1, len(intervals)):
            # Check if there is overlap by confirming if the current itnerval starts before the previous one ends
            if intervals[i][0] < end:
                # Update result
                res += 1
                # Set end to the minimum, as you want to keep the one that ends first
                end = min(end, intervals[i][1])
            else:
                # Update end to be the new interval
                end = intervals[i][1]

        return res