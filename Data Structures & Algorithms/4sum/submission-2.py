class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Generalized, recursive solution

        # Sort the initial input array
        nums.sort()
        
        # Declare array to hold final result
        res = []
        # Declare array to hold current quadruplet
        quad = []

        # Declare helper function to generalize
        def k_sum(k, start, target):
            """
            Pass in:
            k --> number of sums
            start --> starting index
            target --> target the sub-problem is trying to reach
            """
            # What to do when there are more than three digits in k_sum
            if k != 2:
                # Iterate from the starting index to either end of list or to be more efficient, length of the list - k
                for i in range(start, len(nums) - k + 1):
                    # Make sure the value you are at was not already checked
                    if i > start and nums[i] == nums[i - 1]:
                        continue

                    # Append the current value to the quad array
                    quad.append(nums[i])
                    # Call the recursive function
                    k_sum(k - 1, i + 1, target - nums[i])
                    # Once done recursive call, pop this value from the current quad
                    quad.pop()
                return

            # What to do when k == 2
            l, r = start, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    res.append(quad + [nums[l], nums[r]])

                    # Increment l
                    l += 1
                    # Make sure l is not at the same digit
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        # Call k_sum
        k_sum(4, 0, target)
        return res