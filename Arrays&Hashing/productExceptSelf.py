def productExceptSelf(nums: list[int]) -> list[int]: 
    """
    Given an integer array nums, return an array answer such that answer[i] is equal to the product 
    of all the elements of nums except nums[i].
    
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
    
    You must write an algorithm that runs in O(n) time and without using the division operation

    Approach: 
    Prefix and Postfix Sums - 
    An array must be created that's the same size as the input array. Once the array is created, a 
    forward pass of the input array will computer prefix sums of each location in the array. The 
    next step would be to make a backward pass of the input array and compute the postfix sum at each
    index. The prefix sum and the postfix sum multiplied together would result in a product of every
    number except the one at that index. 
    """
    answer = [0 for i in range(len(nums))]

    # Compute the prefix at each location in the nums array
    currPrefix = 1
    answer[0] = 1
    for i in range(1, len(nums)): 
        currPrefix *= nums[i - 1]
        answer[i] = currPrefix

    # Compute the postfix and multiply the postfix by the existing prefix
    currPostfix = 1
    answer[-1] *= currPostfix
    for i in range(len(nums) - 2, -1, -1): 
        currPostfix *= nums[i + 1]
        answer[i] *= currPostfix
    
    return answer 

print("Result:", productExceptSelf([1, 2, 3, 4]))