class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Alternative method: track the farthest end index of a chracter you encounter
        # Create hashmap with the last index at which a character appears
        last_index = {}

        # Even if assigning a number that is not the last index, it will end up assigning the final index
        for i, c in enumerate(s):
            last_index[c] = i

        # Set res array
        res = []
        # Set size and end to be 0 initially
        size = 0
        end = 0

        # Iterate through the string again
        for i, c in enumerate(s):
            # Always increment size
            size += 1
            # Update the end to be the max of the current or where the current letter ends
            end = max(end, last_index[c])

            # Check if the end has been reached
            if i == end:
                res.append(size)
                size = 0

        return res
