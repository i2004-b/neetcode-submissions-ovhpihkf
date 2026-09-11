class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Alternative solution using sorting method:
        Sort the list
        Set the result array to have the first interval in it
        Iterate through the start and end values and compare
            If there is overlap --> merge
            If no overlap --> append new item to the list
        Return the result
        Time: O(nlogn)
        Space: O(n)
        """

        intervals.sort(key = lambda x: x[0])

        res = [intervals[0]]

        for i in range(1, len(intervals)):
            prev_end = res[-1][1]

            new_start = intervals[i][0]
            new_end = intervals[i][1]

            if prev_end >= new_start:
                res[-1][1] = max(prev_end, new_end)
            else:
                res.append(intervals[i])

        return res