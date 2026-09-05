class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Binary Search approach
        # Time: O(n), Space: O(n)

        """
        Approach Idea:
            Use binary search to find where to insert this new interval
            Once you find where to insert it, actually insert into the list (.insert())
            After in place, iterate through the intervals and store values in a result array
                Add value to the result array if res is empty or the beginning value of the interval is greater than the ending value of res[-1]
                Hold off from adding if not the previous conditions and update res[-1][1] to be the max of res[-1][1] and interval[1]
        """

        # If not list
        if not intervals:
            return [newInterval]

        # Set target: beginning of newInterval
        target = newInterval[0]

        # Set pointers
        left, right = 0, len(intervals) - 1

        # Iterate while left is less than right
        while left <= right:
            # Find middle
            mid = (left + right) // 2

            if target > intervals[mid][0]:
                # Move left
                left = mid + 1
            else:
                # Move right
                right = mid - 1

        # Insert the newInterval wherever L ended
        intervals.insert(left, newInterval)

        # Create result array
        res = []

        # Iterate through the intervals
        for interval in intervals:
            # If result does not exist or the end value of the last interval in the result is less than the beginning of the newInterval, add the interval
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            # Else, prepare to merge
            else:
                # Merge by changing the end of res[-1] to be the max of its end and the end of the interval
                res[-1][1] = max(res[-1][1], interval[1])

        return res