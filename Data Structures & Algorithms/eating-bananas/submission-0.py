class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        speed = max(piles)

        while left <= right:
            mid = (left + right) // 2

            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(piles[i] / mid)

            if hours > h:
                left = mid + 1
            else:
                speed = mid
                right = mid - 1
        
        return speed

        