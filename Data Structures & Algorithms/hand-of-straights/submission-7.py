class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        # Create dictionary with the count
        count = Counter(hand)

        hand.sort()

        # Iterate through the numbers in hand
        for num in hand:
            # Check that the count is greater than 0
            if count[num]:
                for n in range(num, num + groupSize):
                    # Check if count in dictionary
                    if not count[n]:
                        return False
                    count[n] -= 1

        return True