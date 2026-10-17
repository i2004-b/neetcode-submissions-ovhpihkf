class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Method 1: Use minheap and dictionary; T: O(nlogn), S: O(n)

        # Step 1: check if the groupSize can be made evenly
        if len(hand) % groupSize:
            return False

        # Step 2: store count of the items
        count = {}
        for h in hand:
            count[h] = 1 + count.get(h, 0)

        # Step 3: make a min_heap with the unique elements
        # Use the keys from the dictionary and make into a list
        min_heap = list(count.keys())

        # Heapify the heap 
        heapq.heapify(min_heap)

        # Iterate while the heap exists
        while min_heap:
            # Try to build the group from the element at the top of heap
            element = min_heap[0]

            for n in range(element, element + groupSize):
                # Check if n exists in the dictionary 
                if n not in count:
                    return False 

                # Decrement n's count
                count[n] -= 1

                # Check if count == 0
                if count[n] == 0:
                    if n == min_heap[0]:
                        heapq.heappop(min_heap)
                    else:
                        return False

        return True



