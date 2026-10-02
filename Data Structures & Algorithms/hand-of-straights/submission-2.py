class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Initial check: see if all the group sizes can be made
        if len(hand) % groupSize != 0:
            return False

        # Create hashmap to keep track of the count of each number
        count = {}

        for h in hand:
            count[h] = 1 + count.get(h, 0)

        # Create a heap with the keys in count
        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        # Iterate while the heap exists
        while min_heap:
            # Get the value at the top of the heap
            top = min_heap[0]

            # Iterate from top value up to top value + groupSize
            for i in range(top, top + groupSize):
                # Check that i is in the dictionary
                if i not in count:
                    return False
                
                count[i] -= 1

                if count[i] == 0:
                    if min_heap[0] != i:
                        return False
                    heapq.heappop(min_heap)
                    
        return True