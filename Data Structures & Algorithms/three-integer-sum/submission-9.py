class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Declare list to hold sublists
        triplets = []

        # Sort the original list
        nums.sort()

        # Iterate through the list
        for i in range(len(nums)):
            # Ensure duplicate triplets are not added
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Declare pointers for the rest of the list
            l = i + 1
            r = len(nums) - 1

            # Iterate through the rest of the list
            while l < r:
                target = nums[i] + nums[l] + nums[r]

                if target > 0:
                    r -= 1
                elif target < 0:
                    l += 1
                else:
                    triplets.append([nums[i], nums[l], nums[r]])

                    # Update l so that it is not at the same number it is at now
                    # Also ensure it is less than right
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1


        return triplets

                    
                    

