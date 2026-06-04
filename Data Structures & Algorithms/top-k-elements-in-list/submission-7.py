class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Declare dictionary
        count = {}

        # Variable to track most frequent items
        most = 0

        # Iterate through the array and add values as well as their frequencies to the count
        for num in nums:
            count[num] = 1 + count.get(num, 0)
            most = max(most, count[num])

        # Create list of lists
        # Have most + 1 because if the most frequent number is, for example, 5, the length of the list needs to be 6 so that 5 is an index
        freq = [[] for _ in range(most + 1)]

        # Iterate through the count and add values to freq
        for key, val in count.items():
            freq[val].append(key)

        # Array to store the result
        res = []

        # Iterate through freq backwards
        for i in range(len(freq) - 1, 0, -1):
            # Iterate for every value in the sublist
            for j in range(len(freq[i])):
                res.append(freq[i][j])
                if len(res) == k:
                    return res