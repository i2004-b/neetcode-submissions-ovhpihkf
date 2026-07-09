class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Most optimal solution: T: O(n), S: O(1)

        # Edge case: is the length of s1 is longer than s2, a permutation cannot be found
        if len(s1) > len(s2):
            return False

        # Declare two arrays that will hold the matches of elements
        s1_count, s2_count = [0] * 26, [0] * 26

        # Iterate through the length of s1_count to get letters of s1 and to get first window of s2_count
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord("a")] += 1
            s2_count[ord(s2[i]) - ord("a")] += 1

        # Set counter for matches, which if 26 means to return True
        matches = 0

        # Iterate through both lists (both of length 26) and update match
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1

        # Sliding window portion
        # Set l to 0
        l = 0
        # Iterate through the list but don't start at 0, start where you left off
        for r in range(len(s1), len(s2)):
            # Check if matches equals 26
            if matches == 26:
                return True

            # Find the index to update
            index = ord(s2[r]) - ord("a") # Letter difference for the index
            # Add to the index
            s2_count[index] += 1

            # Now check the numbers 
            if s1_count[index] == s2_count[index]:
                # Increase matches by 1
                matches += 1
            # if off by 1, decrease matches
            elif s1_count[index] + 1 == s2_count[index]:
                matches -= 1 # This accounts for the initial mismatch and ensures that mismatches is not over decremented


            # Find index of letter to decrement
            index = ord(s2[l]) - ord("a")
            # Decrement from s1_count
            s2_count[index] -= 1

            # If decrement led to a match, update matches with an increase of 1
            if s1_count[index] == s2_count[index]:
                matches += 1
            elif s1_count[index] - 1 == s2_count[index]: # If it just became a mismatch, decrement by 1
                matches -= 1

            # Increment left
            l += 1

        # Return true is matches == 26 else false
        return True if matches == 26 else False
