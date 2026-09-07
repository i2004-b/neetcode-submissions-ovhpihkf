class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        arr of nonoverlaping intervals
        already sorted by start times

        insert the newInterval to keep the order
        merge overlapping intervals
        return intervals

        input: interval[[1, 3], [4, 6]]
        newInt = [2, 5]
        output[[1, 6]]

        0 <= intervals.length <= 10k
        newInterval len == 2

        Be inserted before
        Be inserted after
        Merged --> hardest

        cover lowest and cover the highest --> [1, 5]
        final merge : [1, 6]


        """
        res = []

        for i in range(len(intervals)):
            # Case 1: fits before
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]

        res.append(newInterval)
        return res
        
