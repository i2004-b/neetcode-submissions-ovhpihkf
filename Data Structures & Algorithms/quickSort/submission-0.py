# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs

    def quickSortHelper(self, arr, start, end):
        if (end - start + 1) <= 1:
            return arr

        # Set pivot and initialize the pointer
        pivot = arr[end]
        left = start

        # Order the elements based on relation to the pivot
        for i in range(start, end):
            if arr[i].key < pivot.key:
                arr[left], arr[i] = arr[i], arr[left]
                left += 1

        # Put the pivot in the correct spot
        arr[end] = arr[left]
        arr[left] = pivot

        # Recursive calls
        self.quickSortHelper(arr, start, left - 1)
        self.quickSortHelper(arr, left + 1, end)

        # Return
        return arr

        