class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # Keep count of how many such subarrays exist
        count = 0
        # Multiply threshold by k to optimize by limiting divisions on each iteration of the loop
        threshold *= k
        # Have the current sum of k - 1 items
        curr_sum = sum(arr[0 : k - 1])

        for l in range(len(arr) - k + 1):
            # Add value to curr_sum at right pointer
            curr_sum += arr[l + k - 1]

            if curr_sum >= threshold:
                count += 1

            curr_sum -= arr[l]

        return count