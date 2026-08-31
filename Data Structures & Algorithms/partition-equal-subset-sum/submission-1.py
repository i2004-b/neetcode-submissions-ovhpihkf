class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Check if the sum is odd, in which case, no partition can be made
        if sum(nums) % 2:
            return False

        # Save target
        target = sum(nums) // 2

        # Declare set
        dp = set()
        # Initialize set with 0
        dp.add(0)

        # Iterate through the items in the list
        for i in range(len(nums)):
            # Create new set to add values in
            new_dp = set()

            # Iterate through items in original set
            for n in dp:
                # Check if you arrived at the target
                if n + nums[i] == target:
                    return True

                new_dp.add(n + nums[i])
                # Add old value to new_dp
                new_dp.add(n)

            # Reassign dp to be new_dp
            dp = new_dp

        # Return False
        return False