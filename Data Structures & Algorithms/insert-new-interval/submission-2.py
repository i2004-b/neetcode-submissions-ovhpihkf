class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Linear search method
        # Time: O(n); Space: O(n)

        """
        Method:
            Add values to a result list as long as they end before newInterval begins
            When the conflict occurs, enter into a new loop that will update newInterval to account for merge
            When that loop finishes, add newInterval to the result
            Loop through any remaining values to update result
            return result
        """

        res = []
        i = 0
        length = len(intervals)

        # Add prior intervals
        while i < length and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # Merge intervals
        while i < length and intervals[i][0] <= newInterval[1]:
            # Update newInterval
            newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            i += 1
        # Add merged value
        res.append(newInterval)

        # Add remaining values
        while i < length:
            res.append(intervals[i])
            i += 1

        return res
        