class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Calculate to see if operation is possible
        if len(hand) % groupSize:
            return False

        # Create dictionary with the count
        count = Counter(hand)

        # Create a heap with the keys from the dictionary
        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            # Get the top value
            top = min_heap[0]

            for i in range(top, top + groupSize):
                # If the number does not exist return False
                if i not in count:
                    return False

                # Decrement the count of that number
                count[i] -= 1
                # Check if the count is 0
                if count[i] == 0:
                    if min_heap[0] != i:
                        return False
                    else:
                        heapq.heappop(min_heap)

        return True
