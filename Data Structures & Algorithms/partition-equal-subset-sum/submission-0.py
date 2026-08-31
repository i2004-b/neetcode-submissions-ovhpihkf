class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Check if the sum is odd, in which case you cannot partition
        if sum(nums) % 2:
            return False

        # Set the target value
        target = sum(nums) // 2

        # Create set
        dp = set()
        # Add base case of 0
        dp.add(0)

        # Iterate through the array
        for i in range(len(nums)):
            # Make another set
            newDP = set()

            # Iterate through the items of the old set
            for n in dp:
                # Check if the value is the target
                if n + nums[i] == target:
                    return True

                newDP.add(n + nums[i])
                # Add old values to new set
                newDP.add(n)

            # Reassign dp
            dp = newDP

        return False