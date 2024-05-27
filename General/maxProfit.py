def maxProfit(prices, i, j): 
	if i == j: 
		return 0

	mid = (i + j)//2

	# Find the profit of the left half
	leftHalfProfit = maxProfit(prices, i, mid)

	# Find the profit of the right half
	rightHalfProfit = maxProfit(prices, mid + 1, j)

	# Need to find the max profit of the combined halves
	wholeProfit = findWholeProfit(prices, i, j)

	return max(leftHalfProfit, rightHalfProfit, wholeProfit)

def findWholeProfit(prices, left, right): 
	i = left
	j = left + 1
	maxProfit = 0
	
	while j <= right: 
		if prices[i] >= prices[j]: 
			i = j
			j += 1
		else: 
			newProfit = prices[j] - prices[i]
			maxProfit = max(newProfit, maxProfit)
			j += 1
	
	return maxProfit

prices = [9, 9, 9, 4, 7]
print("Result:", maxProfit(prices, 0, len(prices) - 1))