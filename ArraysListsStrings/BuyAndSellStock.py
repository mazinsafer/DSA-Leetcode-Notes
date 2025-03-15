## O(n) time O(1) space
class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf') ## initialize the min_price (buying price) to inf because we want it to go down
        max_profit = 0 ## start off with a 0 profit
        for price in prices: # iterate through the prices 
            if price < min_price: ## if price is less than the current min_price,
                min_price = price ## its the new min_price
            elif price - min_price > max_profit: ## if the potential profit between the price and current min_price is bigger than the current max profit,
                max_profit = price - min_price ## then that is the new max profit
        return max_profit ## return the max profit