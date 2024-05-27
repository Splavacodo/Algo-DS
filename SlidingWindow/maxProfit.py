def maxProfit(prices: list[int]) -> int: 
    """
    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    You want to maximize your profit by choosing a single day to buy one stock and choosing a 
    different day in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction. If you cannot achieve any 
    profit, return 0.
    """
    # Check if there's only one item in the list before creating pointers
    if len(prices) == 1: 
        return 0 
    
    # Have two pointers that are adjacent to each other
    # The right pointer will check if that day's price is higher or lower
    leftPtr = 0
    rightPtr = 1

    maxProfit = 0

    # The right pointer will always be in front of the left
    while rightPtr < len(prices): 
        # If the price is lower, move both pointers. Otherwise, only move the right
        if prices[leftPtr] < prices[rightPtr]: 
            # Compute the current profit
            currProfit = prices[rightPtr] - prices[leftPtr]
            maxProfit = max(maxProfit, currProfit)
        else: 
            leftPtr = rightPtr 
            
        rightPtr += 1 

    return maxProfit

print("Result:", maxProfit([2, 4, 1]))