class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Iterate through the array and see if the newInterval should be added before, after, or merged
        # Time: O(n)
        # Space: O(n) (for output list)

        # Declare output list
        res = []

        # Iterate through the intervals 
        for i in range(len(intervals)):
            # Case 1: The newInterval should go before the current interval 
            # Compare end of newInterval and beginning of other interval 
            if newInterval[1] < intervals[i][0]:
                # Add newInterval to the result
                res.append(newInterval)
                # Return the result with the rest of the values
                return res + intervals[i:]
            # Case 2: The newInterval should be added after the current interval
            # In this case, add the current interval but do not add the newInterval as it may be merged or put after another interval
            # Compare beginning of newInterval and end of current interval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # Case 3: Merge intervals
            else:
                # Merge by setting beginning to be minimum of both beginnings and the end to be the maximum of both ends
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        # Append interval to list if exited the loop
        res.append(newInterval)

        # Return
        return res