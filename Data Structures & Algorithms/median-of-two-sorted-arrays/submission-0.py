class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Assign the passed in arrays to different variables
        A, B = nums1, nums2

        # Get the sum of the lengths of both arrays and the rought halfway point
        total = len(A) + len(B)
        half = total // 2

        # Only need to run binary search on one of them.
        # For ease, make A the smaller one, and check if it is (if not, swap the arrays)
        if len(B) < len(A):
            A, B = B, A

        # Run binary search on A
        # Get pointers for A
        l, r = 0, len(A) - 1

        # Iterate while True as we are guaranteed to have a median
        while True:
            # Get the middle value of array A
            i = (l + r) // 2
            # Get the index for array B, which is half - i - 2
            j = half - i - 2

            # Get the values to compare the ends to ensure that the partitions are correct
            A_left = A[i] if i >= 0 else float("-inf") # Set to be -inf if out of bounds
            A_right = A[i + 1] if i + 1 < len(A) else float("inf") # Set to be inf it out of bounds
            B_left = B[j] if j >= 0 else float("-inf")
            B_right = B[j + 1] if j + 1 < len(B) else float("inf")

            # Check that the bounds are correct
            if A_left <= B_right and B_left <= A_right:
                # Check whether or not the length is even or odd
                if total % 2 == 1:
                    # If odd, you return the minimum of the right values of both arrays
                    return min(A_right, B_right)
                else:
                    # Add the max of the left values to the minimum of the right values and then divide by 2
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2
            elif A_left > B_right: # Shrink A
                r = i - 1
            else:
                l = i + 1
                
