# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelp(pairs, 0, len(pairs) - 1)


    def mergeSortHelp(self, arr, start, end):
        if end - start + 1 <= 1:
            return arr

        # Caluclate the middle
        mid = (start + end) // 2

        # Call mergeSortHelp on both sides
        self.mergeSortHelp(arr, start, mid)
        self.mergeSortHelp(arr, mid + 1, end)

        # Merge the two halves
        self.merge(arr, start, mid, end)

        return arr
    
    def merge(self, arr, start, mid, end):
        # Copies of the array sides
        left = arr[start: mid + 1]
        right = arr[mid + 1: end + 1]

        # Create pointers for subarrays and main array
        lp = 0
        rp = 0
        mp = start

        # Loop through to place in values
        while lp < len(left) and rp < len(right):
            if left[lp].key <= right[rp].key:
                arr[mp] = left[lp]
                lp += 1
            else:
                arr[mp] = right[rp]
                rp += 1
            mp += 1

        # Loop through remaining items in the list that remains
        while lp < len(left):
            arr[mp] = left[lp]
            lp += 1
            mp += 1
        while rp < len(right):
            arr[mp] = right[rp]
            rp += 1
            mp += 1





