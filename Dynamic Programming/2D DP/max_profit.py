class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit_cache = {}

        def dfs(i, can_buy):
            if i >= len(prices):
                return 0
            elif (i, can_buy) in profit_cache:
                return profit_cache[(i, can_buy)]
            
            hold = dfs(i + 1, can_buy)

            if can_buy:
                buy = dfs(i + 1, not can_buy) - prices[i]
                profit_cache[(i, can_buy)] = max(hold, buy)
            else:
                sell = dfs(i + 2, not can_buy) + prices[i]
                profit_cache[(i, can_buy)] = max(hold, sell)
            
            return profit_cache[(i, can_buy)]

        return dfs(0, True)