class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Set pointers: l is at the minimum (which will be the max weight) and r is at the maximum (sum of the weights)
        l, r = max(weights), sum(weights)
        # Set result to the max (r)
        res = r

        # Iterate while l <= r
        while l <= r:
            # Try middle capacity
            cap = (l + r) // 2

            # Find the number of "ships" this capacity takes
            ships = 1
            rem_cap = cap

            for w in weights:
                if rem_cap - w < 0:
                    # Add to ships
                    ships += 1
                    if ships > days:
                        break
                    # Set rem_cap back to cap
                    rem_cap = cap
                
                # Update remaining cap regularly
                rem_cap -= w

            # If ships is greater than days, then increase the capacity
            if ships > days:
                # Move left l
                l = cap + 1
            else:
                # Update the result
                res = min(res, cap)
                # Update the right pointer
                r = cap - 1

        return res