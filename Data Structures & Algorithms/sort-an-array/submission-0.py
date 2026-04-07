class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums


    def mergeSort(self, arr, left, right):
        if right - left + 1 <= 1:
            return arr

        mid = (right + left) // 2

        self.mergeSort(arr, left, mid)
        self.mergeSort(arr, mid + 1, right)
        self.merge(arr, left, mid, right)
        return arr

    
    def merge(self, arr, left, mid, right):
        # Copies of the arrays
        l_array = arr[left: mid + 1]
        r_array = arr[mid + 1: right + 1]

        # Make pointers
        l = 0
        r = 0
        k = left

        while l < len(l_array) and r < len(r_array):
            if l_array[l] <= r_array[r]:
                arr[k] = l_array[l]
                l += 1
            else:
                arr[k] = r_array[r]
                r += 1

            k += 1

        # Add remaining elements
        while l < len(l_array):
            arr[k] = l_array[l]
            l += 1
            k += 1
        while r < len(r_array):
            arr[k] = r_array[r]
            r += 1
            k += 1


        