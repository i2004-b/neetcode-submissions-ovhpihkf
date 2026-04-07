class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = avg = count = 0

        for right in range(len(arr) + 1):
            if right - left + 1 > k:
                if (avg / k) >= threshold:
                    count += 1
                avg -= arr[left]
                left += 1
            if right < len(arr):
                avg += arr[right]

        return count
        