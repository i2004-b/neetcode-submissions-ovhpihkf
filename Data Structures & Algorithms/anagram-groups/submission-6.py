class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Group the anagrams using a default dictionary set to have lists as the values
        groups = defaultdict(list)

        # Iterate through the words
        for word in strs:
            # Create an array to store the count of each letter
            letters = [0] * 26
            # Iterate through each letter in each word
            for l in word:
                # Update the count for each letter in the array
                letters[ord(l) - ord("a")] += 1

            # Create an immutable key by making the letters list a tuple
            key = tuple(letters)
            # Append to that key the word
            groups[key].append(word)

        # Return the result, which is all the values in one array
        return [val for val in groups.values()]