class FreqStack:
    """
    Brute Force Solution:
    Implements the stack with push working in O(1) but pop working in O(n).
    Keep a count of the number of times each number shows up in the stream of numbers.
    Have a stack to track the order of the items.

    When you push, increment the count and add to the stack.

    When you pop, get the max count by looking through the dictionary.
    Then find the value that most recently appeared in the stack by working backward and checking each item's frequency.
    Once you find this item's index, return the item by popping at that index (O(n)).
    """
    def __init__(self):
        # Declare stack
        self.stack = []
        # Declare hashmap to track the count
        self.cnt = {}


    def push(self, val: int) -> None:
        self.stack.append(val)
        self.cnt[val] = 1 + self.cnt.get(val, 0)


    def pop(self) -> int:
        # Get the max count
        maxCnt = max(self.cnt.values())
        # Set a pointer to the last index
        i = len(self.stack) - 1

        # Iterate through the list to find the most recently added item with the max count
        while self.cnt[self.stack[i]] != maxCnt:
            i -= 1

        # Once you get the value that is equal to the maxCount, update the count in the self.cnt dictionary and pop it
        self.cnt[self.stack[i]] -= 1
        return self.stack.pop(i)



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()



