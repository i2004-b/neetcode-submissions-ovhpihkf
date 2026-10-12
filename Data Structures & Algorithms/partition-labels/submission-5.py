class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        s --> has lowercase letters
        split into substrings and ensure each letter appears in at most one substring

        given string
        traverse string through a loop one-pass
        keep count of the letters in the string 
        we should also use a set for each substring 
        add to set when we see a letter
        once we see letter we decrement the count and if the count is 0, we remove from set

        have a results array to hold the lengths (keep count of the results and set to 0 when we see a new one)
        """

        letters = Counter(s)

        sub = set()
        cnt = 0
        res = []

        for c in s:
            if c not in sub:
                sub.add(c)
            
            cnt += 1
            letters[c] -= 1

            if letters[c] == 0:
                sub.remove(c)
            
            if not sub:
                res.append(cnt)
                cnt = 0

        return res
