class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [0]
        self.k = k

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        self.heap.append(val)

        # Get location of last element
        i = len(self.heap) - 1

        # Reorganize heap
        while i > 1 and self.heap[i] < self.heap[i // 2]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2

        
        # Pop when the heap has more than k values
        if len(self.heap) - 1 > self.k:
            # Pop values --> reassign top value
            self.heap[1] = self.heap.pop()
            # Set pointer to the top element to make sure everything is in order
            i = 1

            while 2 * i < len(self.heap):
                # Check that right child exists
                if (2 * i + 1 < len(self.heap) and
                self.heap[2 * i + 1] < self.heap[2 * i] and
                self.heap[2 * i + 1] < self.heap[i]):
                    self.heap[i], self.heap[2 * i + 1] = self.heap[2 * i + 1], self.heap[i]
                    i = 2 * i + 1
                elif self.heap[2 * i] < self.heap[i]:
                    self.heap[i], self.heap[2 * i] = self.heap[2 * i], self.heap[i]
                    i = 2 * i
                else:
                    break


        return self.heap[1]
        


    
        
