class Solution:
    def mySqrt(self, x: int) -> int:
        # Declare left and right pointers
        l, r = 0, x
        # Declare a variable to track the rounded down integer
        sqrt = 0

        # Iterate while the left pointer does not pass the right pointer
        while l <= r:
            # Calculate the middle number
            mid = (r + l) // 2

            # If the middle number squared is less than x, update sqrt as long as the new number is greater than it
            if mid ** 2 < x:
                sqrt = mid
                l = mid + 1
            elif mid ** 2 > x:
                r = mid - 1
            else:
                return mid

        return sqrt