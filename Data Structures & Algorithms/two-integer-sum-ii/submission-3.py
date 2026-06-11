class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Have pointer to the beginning and the end of the list
        i, j = 0, len(numbers) - 1

        # Iterate through the list
        """
        Algorithm: 
        if sum is greater than target, move upper val down
        if sum less than target, move lower val up
        if sum equal to target, return the indices + 1
        """

        # i and j cannot be equal
        while i < j:
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                # Guaranteed to get a solution so return inside the loop
                return [i + 1, j + 1]
        