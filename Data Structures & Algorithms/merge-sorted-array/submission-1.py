class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Time Complexity: O(m + n) where m is the number of elements in nums1 and n is the number of elements in nums2
        # Space Complexity: O(m), where m is the number of elements in nums1. This is needed for the array copy.
        # Make copy of nums1 values because nums1 is being overwritten
        nums1_copy = nums1[:m + 1]

        # Pointers for nums1_copy, nums2, and nums1, respectively
        i = j = k = 0

        # Iterate while the pointers are still within bounds
        while i < m and j < n:
            # Check for <= to keep algorithm stable
            if nums1_copy[i] <= nums2[j]:
                nums1[k] = nums1_copy[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j +=1

            # Increment the pointer in the original array
            k += 1

        # Handling any remaining numbers within the lists
        while i < m:
            nums1[k] = nums1_copy[i]
            i += 1
            k += 1
        while j < n:
            nums1[k] = nums2[j]
            j += 1
            k += 1

