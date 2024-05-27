def longestConsecutive(nums: list[int]) -> int: 
    """
    Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

    You must write an algorithm that runs in O(n) time.

    Approach: 
    Go through every number in the input array and add it to a set. After a set is created, go through each number in the
    input array again and check if the current number is the start of a sequence. Once the start of a sequence has been 
    recognized, check for rest of the numbers in the sequence using a while loop. 
    """
    # Create a set that contains the numbers in the input array 
    numsSet = set(nums)
    longestSeq = 0 

    for num in nums: 
        if num - 1 not in numsSet: 
            length = 0
            while num + length in numsSet: 
                length += 1
            longestSeq = max(length, longestSeq)
    return longestSeq

print("Result:", longestConsecutive([100, 4, 200, 1, 3, 2]))