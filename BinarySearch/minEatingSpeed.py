from math import ceil 
def minEatingSpeed(piles: list[int], h: int) -> int: 
    """
    Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
    The guards have gone and will come back in h hours.

    Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of 
    bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all 
    of them instead and will not eat any more bananas during this hour.

    Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

    Return the minimum integer k such that she can eat all the bananas within h hours.
    """
    # Where to start bounds for searching the optimal k? 
    # Initial thought is to have the bounds go from 1 to the max int in the piles list, any eating
    # speed greater than the max pile won't be useful

    # When should the search stop? When the eating speed is no longer valid 

    # How to know if a speed is valid? 
    # Need to go through every number in the piles list and check if each pile can be eaten

    # Create a range of possible k values given the max number of bananas in a pile
    # using two pointers
    leftPtr = 1
    rightPtr = max(piles)
    
    # Start the min eating speed to the max speed
    minSpeed = rightPtr 

    # Continue search for an optimal k until the pointers cross each other
    while leftPtr <= rightPtr: 
        currK = (leftPtr + rightPtr) // 2
        
        # Check if the current k is good enough to clear all the piles
        hoursUsed = 0 

        for pile in piles: 
            if pile <= currK: 
                hoursUsed += 1
            else: 
                hoursUsed += ceil(pile/currK)
        
        if hoursUsed <= h: 
            minSpeed = min(currK, minSpeed)
            rightPtr = currK - 1
        else: 
            leftPtr = currK + 1
    
    return minSpeed

print("Result:", minEatingSpeed([3,6,7,11], 8))