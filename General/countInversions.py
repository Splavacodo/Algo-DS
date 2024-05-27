def countInversions(nums, i, j):
	if i == j:
		return 0

	inversions = 0
	
	mid = (i + j)//2
	inversions += countInversions(nums, i, mid)
	inversions += countInversions(nums, mid + 1, j)
	inversions += countMergedInversions(nums, i, mid, j)
	
	return inversions

def countMergedInversions(nums, i, mid, j): 
	B = [0 for _ in range(j-i + 1)]
	a = i
	c = mid + 1
	b = 0 
	inversions = 0 

	while a <= mid and c <= j:
		if nums[a] < nums[c]: 
			B[b] = nums[a]
			a += 1
		else: 
			B[b] = nums[c]
			c += 1
			inversions += (mid - a + 1)
		b += 1

	while a <= mid: 
		B[b] = nums[a]
		a += 1
		b += 1

	while c <= j: 
		B[b] = nums[c]
		c += 1	
		b += 1
	
	b = 0 
	for k in range(i, j + 1): 
		nums[k] = B[b]
		b += 1
	return inversions

# nums = [i for i in range(5, 0, -1)]
nums = [5, 4, 3, 2, 1]
inversions = countInversions(nums, 0, len(nums) - 1)
print(inversions)