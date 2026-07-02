class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Set the boundaries
        l, r = max(weights), sum(weights)
        # Set intial result
        res = r

        # Declare helper function to check if capacity will achieve goal
        def can_ship(cap):
            # Set the number of ships to 1 because need at least 1 ship
            ships = 1
            # Set the remaining capapcity to the capacity that is passed in
            rem_cap = cap

            # Iterate through all the weights in weights
            for w in weights:
                # Check if subtracting the weight will result in a negative number
                if rem_cap - w < 0:
                    # Increment the number of ships
                    ships += 1
                    # Reset the capacity
                    rem_cap = cap

                # Update the rem_cap by subtracting the weight from it
                rem_cap -= w
            
            return ships <= days

        # Perform binary search
        while l <= r:
            # Select capacity to test
            cap = (l + r) // 2

            if can_ship(cap): # If ships is fine, set result to the minimum and update the right
                res = min(res, cap)
                r = cap - 1
            else: # if days are over, you need to go faster
                l = cap + 1

        return res
