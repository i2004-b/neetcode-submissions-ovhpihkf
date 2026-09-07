class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # Comes before: can add newInterval, add the rest of the items, and then return
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # Comes after
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                # Update the newInterval to encompass the interval at i and the current values of newInterval
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]

        res.append(newInterval)

        return res