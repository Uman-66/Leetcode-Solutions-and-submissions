class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        profit = 0
        for i in range(len (prices)):
            if(min > prices[i]):
                min = prices[i]
            if(prices[i] - min ) > profit:
                profit = prices[i] - min
        return profit

            
        