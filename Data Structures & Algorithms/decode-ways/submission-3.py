class Solution:
    def numDecodings(self, s: str) -> int:
        dec1, dec2 = 1, 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                curr = 0
            else:
                curr = dec1

            if (i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456")):
                curr += dec2

            dec1, dec2 = curr, dec1
        
        return dec1
                