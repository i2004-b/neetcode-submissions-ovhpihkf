class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Declare pointers to each array
        i = m - 1
        j = n - 1
        k = m + n - 1

        # Iterate while both pointers are in bounds
        while i >= 0 and j >= 0:
            # Compare
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        # Check to see if there are still items in nums2
        if j >= 0:
            nums1[: j + 1] = nums2[: j + 1]

        
