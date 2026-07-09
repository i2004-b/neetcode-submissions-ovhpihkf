class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Solution 2 (slightly optimized): T: O(n), S: O(m)
        # This solution tracks the max_frequency and only updates it if it increases

        count = {}

        res = 0
        max_freq = 0

        l = 0

        for r in range(len(s)):
            # Update count
            count[s[r]] = 1 + count.get(s[r], 0)
            # Update max_freq is needed
            max_freq = max(max_freq, count[s[r]])

            # Update the left pointer if needed
            while (r - l + 1) - max_freq > k:
                # Decrement item at left
                count[s[l]] -= 1
                # Update left
                l += 1

            # Update result
            res = max(res, r - l + 1)
            
        return res
        