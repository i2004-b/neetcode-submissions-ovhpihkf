class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # Keep track of the number of results
        res = 0

        # Get the current sum of the values of k - 1 values
        # k is 3 values, not the difference between the indexes
        curr_sum = sum(arr[:k - 1])

        # Have a left pointer iterating through
        for l in range(len(arr) - k + 1):
            # add the value of the "right pointer"
            # which is l + k
            curr_sum += arr[l + k - 1]

            # Check if curr_sum / k is threshold and update count
            if curr_sum / k >= threshold:
                res += 1

            # Take away the item from the left
            curr_sum -= arr[l]

        return res

