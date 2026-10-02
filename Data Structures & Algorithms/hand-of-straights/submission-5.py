class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Check if the groupSize can be made
        if len(hand) % groupSize:
            return False

        # Make a count of the values 
        count = Counter(hand)

        # Sort the list 
        hand.sort()

        # Pointer to the minimum value in hand
        i = 0

        # Iterate while i < len(hand)
        while i < len(hand):
            # Save the minimum value
            top = hand[i]

            # Iterate for the groupSize items
            for j in range(top, top + groupSize):
                # Check if that number is in count
                if j not in count:
                    return False

                count[j] -= 1
                # Check if the count has become 0
                if count[j] == 0:
                    if hand[i] != j:
                        return False
                    
                    curr = hand[i]
                    while i < len(hand) and hand[i] == curr:
                        i += 1

        return True


