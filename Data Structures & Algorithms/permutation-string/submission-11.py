class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Most optimal retry

        # First check if the length of s1 is longer than s2, in which case return false
        if len(s1) > len(s2):
            return False

        # Create two arrays to hold the letter count for each word
        s1_count = [0] * 26
        s2_count = [0] * 26

        # Add the letter counts for s1 and the first window of s2
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord("a")] += 1
            s2_count[ord(s2[i]) - ord("a")] += 1

        # Keep track of the number of matches
        matches = 0

        # Iterate through both lists and check equality of items. If equal, increment matches
        for i in range(26): # Both are of length 26 so both work
            if s1_count[i] == s2_count[i]:
                matches += 1

        # Intialize left pointer
        l = 0
        
        # Search through the remaining windows
        for r in range(len(s1), len(s2)):
            # Return if matches is already equal to 26
            if matches == 26:
                return True

            # Get the letter at the right pointer
            index = ord(s2[r]) - ord("a")
            s2_count[index] += 1

            # Check if matches needs to be updated
            if s1_count[index] == s2_count[index]:
                matches += 1
            elif s1_count[index] + 1 == s2_count[index]:
                matches -= 1

            
            # Remove item at the current left pointer
            index = ord(s2[l]) - ord("a")
            # Subtract from that index
            s2_count[index] -= 1

            if s1_count[index] == s2_count[index]:
                matches += 1
            elif s1_count[index] - 1 == s2_count[index]:
                matches -= 1

            # Increment the left pointer
            l += 1

        # Return true if matches == 26 else return false
        return True if matches == 26 else False

            