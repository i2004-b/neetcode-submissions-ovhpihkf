class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        l = 0
        r = 0
        window = {}
        while r < len(nums):
            while r < k - 1:
                window[nums[r]] = 1 + window.get(nums[r], 0)
                r += 1
    
            window[nums[r]] = 1 + window.get(nums[r], 0)
            output.append(max(window))
            # remove the element at the left
            window[nums[l]] -= 1
            if window[nums[l]] == 0:
                del window[nums[l]]
            
            # Update the pointers
            l += 1
            r += 1

        return output
