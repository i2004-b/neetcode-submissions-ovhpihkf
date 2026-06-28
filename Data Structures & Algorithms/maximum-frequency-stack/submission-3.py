class FreqStack:
    """
    Most Optimal Solution: Use a dictionary with stacks as values to the keys
    Push --> O(1)
    Pop --> O(1)
    """
    def __init__(self):
        self.cnt = {}
        self.stacks = {}
        self.max_cnt = 0

    def push(self, val: int) -> None:
        self.cnt[val] = 1 + self.cnt.get(val, 0)
        # Add stack if needed and update max_cnt
        if self.cnt[val] > self.max_cnt:
            self.max_cnt = self.cnt[val]
            self.stacks[self.max_cnt] = []
        self.stacks[self.cnt[val]].append(val)


    def pop(self) -> int:
        res = self.stacks[self.max_cnt].pop()
        self.cnt[res] -= 1
        if not self.stacks[self.max_cnt]:
            #self.max_cnt = self.cnt[res]
            self.max_cnt -= 1

        return res

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()