class Solution:
    def trap(self, height: List[int]) -> int:
        # T: O(n) and S: O(n) solution
        length = len(height)

        prefix = [0] * length
        for i in range(length):
            if i == 0:
                prefix[i] = height[i]
            else:
                prefix[i] = max(height[i], prefix[i - 1])

        suffix = [0] * length
        for i in range(length - 1, -1, -1):
            if i == length - 1:
                suffix[i] = height[i]
            else:
                suffix[i] = max(height[i], suffix[i + 1])

        # Calculate sum
        sol = 0
        for i in range(length):
            val = min(prefix[i], suffix[i]) - height[i]
            if val >= 0:
                sol += val

        return sol