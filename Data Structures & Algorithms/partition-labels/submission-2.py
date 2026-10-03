class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Array that will hold output
        res = []
        # Keep count for current substring
        length = 0
        # Set for the elements in the current group
        curr = set()

        # Create dictionary with counts of the string 
        count = Counter(s)

        # Iterate through the string
        for i in s:
            # Add to the set
            curr.add(i)
            # Increase length of substring
            length += 1
            # Decrement count of that letter
            count[i] -= 1

            # Check count
            if not count[i]:
                curr.remove(i)

            if not curr:
                res.append(length)
                length = 0

        return res