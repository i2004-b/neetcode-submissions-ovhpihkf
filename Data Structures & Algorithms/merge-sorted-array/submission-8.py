class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Single loop solution

        # Declare pointers
        i, j = m - 1, n - 1
        k = m + n - 1

        # Iterate thorugh as long as j in range of nums2 elements
        while j >= 0:
            # Add item from nums1 is i exists and if it is greater than nums2
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1

