class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupings = defaultdict(list)

        for word in strs:
            char_arr = [0] * 26 # To store the count of which letters show up

            for letter in word:
                char_arr[ord(letter) - ord("a")] += 1
            groupings[tuple(char_arr)].append(word)

        return list(groupings.values())