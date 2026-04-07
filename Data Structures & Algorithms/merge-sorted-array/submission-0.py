class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Iterate through the second half of nums2
        for i in range(n):
            nums1[m + i] = nums2[i]

        # Sort nums1
        nums1.sort()