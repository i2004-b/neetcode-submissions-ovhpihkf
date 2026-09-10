class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Solution description:
        Step 1: Sort values based on starting values (easier to compare intervals and subsequently merge them)
        Step 2: Create an array that will hold the merged intervals (res)
        Step 3: Assign a variable that will hold the interval that needs to be added (assign to first item in interval array)
        Step 4: Loop through the intervals (from index 1 to the end)
            a) If the end of the merged interval is less than the start of the current interval:
                add interval in merge variable to res
                set merge to the current interval
            b) If the end of the merged interval is greater than or equal to the start of the current interval:
                merge the intervals --> left bound is the minimum of both left bounds and the right bound is the maximum of boths right bounds
        Step 5: Add the last merged item to the result List
        Step 6: Return the result List

        Time: O(n log n)
        Space: O(n)
        """

        # Sort values based on the starting values
        intervals.sort(key=lambda x: x[0])

        # Create array to hold result
        res = []

        # Set merged variable
        merge = intervals[0]

        # Iterate
        for i in range(1, len(intervals)):
            # Add merge to result
            if merge[1] < intervals[i][0]:
                res.append(merge)
                merge = intervals[i]
            else:
                merge = [min(merge[0], intervals[i][0]), max(merge[1], intervals[i][1])]

        # Add final merge to the result
        res.append(merge)

        return res