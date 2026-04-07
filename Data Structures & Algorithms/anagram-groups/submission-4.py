class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            letter_count = [0] * 26

            for letter in word:
                letter_count[ord(letter) - ord("a")] += 1

            groups[tuple(letter_count)].append(word)

        return list(groups.values())
        