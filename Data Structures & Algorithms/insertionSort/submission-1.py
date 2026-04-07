# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        # Sort by the key
        # Return list of lists, so need to append the list to the list

        n = len(pairs)
        result = []

        for i in range(n):
            j = i - 1

            while j >= 0 and pairs[j].key > pairs[j + 1].key:
                pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]
                j -= 1
            
            # Need to do [:] because it is an object being modified
            # Use [:] to clone
            # The following line does impact time complexity -> O(n^3)
            result.append(pairs[:])

        return result