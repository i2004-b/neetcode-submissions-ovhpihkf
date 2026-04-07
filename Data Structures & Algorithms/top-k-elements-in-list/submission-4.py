class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        frequency = [[] for _ in range(len(nums) + 1)]

        for value in nums:
            count[value] = 1 + count.get(value, 0)

        for key, value in count.items():
            frequency[value].append(key)

        res = []

        for i in range(len(frequency) - 1, 0, -1):
            for num in frequency[i]:
                res.append(num)

                if len(res) == k:
                    return res
        
        
        
        
        
        # freq = {}

        # for num in nums:
        #     freq[num] = 1 + freq.get(num, 0)

        # arr = []
        # for key, value in freq.items():
        #     arr.append([value, key])

        # arr.sort()

        # res = []

        # while k > 0:
        #     max_f = arr.pop()
        #     res.append(max_f[1])
        #     k -= 1

        # return res