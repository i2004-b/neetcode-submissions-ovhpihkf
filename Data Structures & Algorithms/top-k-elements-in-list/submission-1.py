class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        arr = []
        for key, value in freq.items():
            arr.append([value, key])

        arr.sort()

        res = []

        while k > 0:
            max_f = arr.pop()
            res.append(max_f[1])
            k -= 1

        return res