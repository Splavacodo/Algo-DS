class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        # each row represents a different coin
        # each col represents a different amount
        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins))]

        # one base case is if you have no amount
        # if there's no amount, the only combination is to include no coins
        for row in range(len(coins)):
            dp[row][0] = 1
        
        # the other base case is if you can make a combination only using the first coin for different amounts
        coin = coins[0]

        for amt in range(1, amount + 1):
            if amt % coin == 0:
                dp[0][amt] = 1
        
        for i in range(1, len(coins)):
            coin = coins[i]

            for amt in range(1, amount + 1):
                if amt - coin >= 0:
                    dp[i][amt] = dp[i][amt - coin] + dp[i - 1][amt]
                else:
                    dp[i][amt] = dp[i - 1][amt]
        
        return dp[-1][-1]