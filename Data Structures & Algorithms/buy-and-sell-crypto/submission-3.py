class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        future_maximum_price = [0]
        maximum_price = prices[-1]
        for i in prices[-2::-1]:
            future_maximum_price.append(maximum_price)
            maximum_price = max(maximum_price, i)
        future_maximum_price = future_maximum_price[::-1]

        best_trade = 0
        for i in range(0, len(prices)-1):
            best_trade = max(best_trade, future_maximum_price[i]-prices[i])

        return best_trade