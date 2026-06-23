class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1 # Span starts at 1 for every number

        while self.stack and self.stack[-1][1] <= price: # Iterate while the stack exists and the top of the stack is less than or equal to price
            day, money = self.stack.pop()
            span += day

        self.stack.append((span, price))
        return span



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)