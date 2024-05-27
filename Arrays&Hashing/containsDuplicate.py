def containsDuplicate(intArr: list[int]) -> bool: 
    '''
    Given an integer array nums, return true if any value appears at least twice in the array, 
    and return false if every element is distinct.


    Different Approaches: 

    Brute Force - 
    Compare each num in the array to every other number in the array using two for loops
        Time Complexity: O(n^2)
        Space Complexity: O(1)
    
    Sort the Array - 
    First sort the array and then have two pointers that will go through each number in 
    the array. Duplicates would be guaranteed to be next to each other. 
        Time Complexity: O(nlogn)
        Space Complexity: O(1)
    
    Use a set to keep track of duplicates - 
    Create a set and add all the numbers in the input array into the hashset. As the numbers are
    added into the hashset, see if the set contains that number first. If the set already contains
    the number wanting to be added, it's a duplicate. 
        Time Complexity: O(n)
        Space Complexity: O(n)
    '''
    # Create an empty set to keep track of counts
    occurenceCount = set()

    # Loop through the numberes in the array and check if getting a key returns a default value of 0 
    for num in intArr: 
        if num in occurenceCount: 
            return True 
        occurenceCount.add(num)
    return False 

print(containsDuplicate([1, 2, 3, 4]))