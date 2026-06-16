class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Count Sort Method
        count = [0] * (limit + 1)

        for p in people:
            count[p] += 1

        index = 0
        for idx, val in enumerate(count):
            for _ in range(val):
                people[index] = idx
                index += 1

        l, r = 0, len(people) - 1
        res = 0

        while l <= r:
            remain = limit - people[r]
            r -= 1
            res += 1

            if l <= r and remain >= people[l]:
                l += 1
        
        return res

                

        