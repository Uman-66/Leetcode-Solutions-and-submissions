class StockSpanner:
    def __init__(self):
        # stack stores pairs: (price, span) for decreasing prices
        self.stack = []

    def next(self, price: int) -> int:
        span = 1  # today always counts
        # Pop all smaller or equal prices from the stack
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        # Push current price with its span
        self.stack.append((price, span))
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)