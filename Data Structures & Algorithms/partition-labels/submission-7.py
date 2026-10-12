class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        Another approach would be to look at the last indices
        We track when a character appears last so that we know the substring goes up until that point --> need dictionary and loop for it
        
        Single letters are easy as you append 1
        encounter a letter: check where it ends and update a target variable 
        cnt above
        i == t: add the result
        set counter to be 0

        iterate through the string 
        0 1 2 3 4.  5 6 7 8 9 10 11 12
        x y x x y.  z b z b b i  s  l
        i                 t i

        {
            x: 3
            y: 4
            z: 7
            b: 9
            i: 10
            s: 11
            l: 12 
        }
        """

        last = {}

        # Iterate to get value and index (enumerate)
        for ind, val in enumerate(s):
            last[val] = ind

        res = [] # [5, 5
        cnt = 0 # 
        target = 0 # 9

        for i in range(len(s)):
            target = max(target, last[s[i]])
            cnt += 1

            # Check if i == target
            if i == target:
                # Append cnt to result 
                res.append(cnt)
                # Set cnt to 0
                cnt = 0

        return res

