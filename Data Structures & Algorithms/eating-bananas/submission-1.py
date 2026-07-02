class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Find the max pile amount (this is the min_speed if h == len(piles))
        max_b = max(piles)
        # Declare variable to hold the minimum speed
        min_speed = float("inf")
        # Declare pointers to point to the bounds of the range of speeds
        l, r = 1, max_b

        # Iterate while l is <= r
        while l <= r:
            # Find a speed to test
            speed = (l + r) // 2

            # Track hours that this speed takes
            hours = 0
            # Iterate through the list with the speed
            for num in piles:
                hours += math.ceil(num / speed)

            # Update the speed only if the hours was less than or equal to h and the new speed is lower
            # If the hours were greater than the speed, update the left pointer
            if hours > h:
                l = speed + 1
            elif hours <= h:
                r = speed - 1
                min_speed = min(min_speed, speed)

        return min_speed