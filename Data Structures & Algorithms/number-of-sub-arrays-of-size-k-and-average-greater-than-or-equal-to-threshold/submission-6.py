class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        threshold *= k
        curr_sum = 0

        for r in range(len(arr)):
            curr_sum += arr[r]

            if r >= k - 1:
                if curr_sum >= threshold:
                    count += 1
                # Subtract the "left pointer" value
                curr_sum -= arr[r - k + 1]
        return count