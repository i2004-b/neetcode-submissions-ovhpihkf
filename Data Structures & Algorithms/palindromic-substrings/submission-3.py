class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0

        for i in range(len(s)):
            l = r = i

            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    cnt += 1
                    l -= 1
                    r += 1
                else:
                    break

            l, r = i, i + 1

            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    cnt += 1
                    l -= 1
                    r += 1
                else:
                    break

        return cnt