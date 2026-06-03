class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Use hash map to keep track of the count values
        count = {}

        # Declare array to hold values according to frequency
        freq = [[] for _ in range(len(nums) + 1)]

        # Add values to the count dictionary
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Go through the dictionary and add values correctly based on frequency
        for num, cnt in count.items():
            freq[cnt].append(num)

        # Declare array to hold result
        res = []

        # Iterate backwards to get most frequent elements and add to the result
        # Can stop before 0th index because 0th index will hold an empty array
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
