def topKFrequent(nums: list[int], k: int) -> list[int]: 
    """
    Given an integer array nums and an integer k, return the k most frequent elements. 
    You may return the answer in any order

    Different Approaches: 
    Max Heap - 
    The idea is to create a hashmap of occurences for each number in the nums list. Once the hashmap
    is built, the pairs in the map can be added to a max heap. After the entire heap is built, k pops
    can be done on the heap and those numbers can be added to a list.  
        Time Complexity: O(k*logn + n)
        Space Complexity: O(n)
    
    Bucket Sort - 
    A hashmap of occurences for each number in the nums list needs to be built first. After the map is built,
    an array of nested arrays can be created. This array should be the size of the nums list, with each index
    representing a number of occurences. Depending on the occurence of a number, the number will be placed in
    the array at that index. Once each number is placed in a bucket, the list will be looped through starting
    from the last bucket which represents the highest number of occurences. 
        Time Complexity: O(n)
        Space Complexity: O(n)
    """ 
    # Create a hashmap with each number as the key, and then have the value be
    # the number of occurences for that number
    occurences = {}

    for num in nums: 
        occurences[num] = occurences.get(num, 0) + 1
    
    # After the hashmap has been built, add the number of occurences to a list
    # The catch is that the list should be the size of the nums list where each 
    # index represents the number of occurences. This means there's a nested list
    # at each index
    buckets = [[] for i in range(len(nums) + 1)]

    for num, occurence in occurences.items(): 
        buckets[occurence].append(num)

    # Once the buckets have been filled, start at the very end and see which numbers have
    # the most occurences
    topKFrequent = []
    for i in range(len(buckets) - 1, -1, -1): 
        for num in buckets[i]: 
            topKFrequent.append(num)
            if len(topKFrequent) == k: 
                return topKFrequent
    

print("Result:", topKFrequent([3,0,1,0], 1))