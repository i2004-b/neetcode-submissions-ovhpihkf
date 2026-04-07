class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        arr = []
        for key, value in freq.items():
            arr.append([value, key])

        arr.sort(reverse=True)

        return_arr = []
        for i in range(k):
            return_arr.append(arr[i][1])

        return return_arr