class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        buy = prices[0]
        sell = prices[0]
        max_profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
                sell = prices[i]  
            elif prices[i] > sell:
                sell = prices[i]
                max_profit = max(max_profit, sell - buy)
        
        return max_profit
