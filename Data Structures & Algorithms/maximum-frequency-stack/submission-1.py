class FreqStack:
    """
    Heap Solution:
    Implements the stack but the push and the pop would work in O(log(n)).
    Implement the stack as a max heap. Need to also have a dictionary that holds the count of each time the value has been encountered.
    Keep track of the index that you are at for the "stack" as well

    When pushing an item, push to the heap the (neg) count, (neg) index, and the val
    """
    def __init__(self):
        # Declare the heap
        self.heap = []
        # Declare the count dictionary
        self.cnt = {}
        # Declare the index tracker
        self.index = 0


    def push(self, val: int) -> None:
        # Update the count in the dictionary
        self.cnt[val] = 1 + self.cnt.get(val, 0)
        # Add tuple to mimic the stack's property of trying to get the most recently added
        heapq.heappush(self.heap, (-self.cnt[val], -self.index, val))
        # Increment the index
        self.index += 1

    def pop(self) -> int:
        _, _, val = heapq.heappop(self.heap)
        self.cnt[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()