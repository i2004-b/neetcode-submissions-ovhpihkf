class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Method 1: Sorting; T: O(nlogn), S: O(n)

        # Step 1: check divisibility by groupSize 
        if len(hand) % groupSize:
            return False

        # Step 2: count frequency of the items
        count = {}
        for h in hand:
            if h not in count:
                count[h] = 0
            count[h] += 1

        # Step 3: sort the list
        hand.sort()

        # Step 4: Iterate through the list 
        for h in hand:
            # Check if the current card has already been used, in which case, you should skip it 
            if count[h] == 0:
                continue
            
            # Otherwise, try to form a group from here
            # Want to ensure that every number from the current to the current + groupSize exists/still exists
            for n in range(h, h + groupSize):
                if n not in count or count[n] == 0:
                    return False
                count[n] -= 1

        # If everything else worked, can return True
        return True