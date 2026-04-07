class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # In each spot will hold a list containing the words
        groups = collections.defaultdict(list)

        for word in strs: # Num of strings is n
            char_count = [0] * 26

            for letter in word: # number of char(lowest) is m
                index = ord(letter) - ord("a")
                char_count[index] += 1

            alphabetized_string = ""
            for index, value in enumerate(char_count): 
                unicode_value = index + ord("a")
                char_value = chr(unicode_value)

                for _ in range(value):
                    alphabetized_string += char_value

            groups[alphabetized_string].append(word)

        return_list = [array for array in groups.values()]
        return return_list