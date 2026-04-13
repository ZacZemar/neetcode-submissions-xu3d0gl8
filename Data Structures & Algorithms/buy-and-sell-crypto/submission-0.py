class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        profit = 0

        while sell < len(prices):
            if prices[sell] < prices[buy]:
                buy = sell
            elif prices[buy] < prices[sell]:
                profit = max(profit, prices[sell] - prices[buy])
            sell += 1
        return profit

# example = [7,1,5,6,4,3]