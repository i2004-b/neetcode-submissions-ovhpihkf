class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # List to hold array of quadruplets
        quad = []

        # Sort the array to use the two sum method
        nums.sort()

        # Iterate over the entire list (first item in quad)
        for i in range(len(nums)):
            # Check that the value has not already been accounted for
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Iterate over the remaining values in the list (second item in quad)
            for j in range(i + 1, len(nums)):
                # Check that the value has not already been accounted for
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # Declare pointers to run two sum
                l, r = j + 1, len(nums) - 1

                # Two sum algorithm
                while l < r:
                    curr = nums[i] + nums[j] + nums[l] + nums[r]

                    if curr > target:
                        r -= 1
                    elif curr < target:
                        l += 1
                    else:
                        quad.append([nums[i], nums[j], nums[l], nums[r]])

                        # Increment l
                        l += 1

                        # Check that l is not at the same value as before
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
        
        return quad

