def validAnagram(firstStr: str, secondStr: str): 
    """
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
    typically using all the original letters exactly once.

    Different Approaches: 
    Hashmaps - 
    Two hashmaps could be used to count the occurences of each letter in each string. Once the hashmaps
    are built, the keys and the occurences can be compared. If either a key or a number of occurences is
    different, the two strings can't be anagrams. 
        Time Complexity: O(len(firstStr) + len(secondStr))
        Space Complexity: O(len(firstStr) + len(secondStr))
    
    Counter - 
    In python there's a built in Counter method in a module that does the same thing as the hashmap approach. A solution
    in python could then be one line of code that checks if Counter(firstStr) == Counter(secondStr)
        Time Complexity: O(len(firstStr) + len(secondStr))
        Space Complexity: O(len(firstStr) + len(secondStr))

    Sorting - 
    The two strings can be sorted then the resulting strings can be compared to each other. 
        Time Complexity: O(nlogn)
        Space Complexity: O(n)/O(1)...depends on the sorting algorithm that's used
    """
    # A simple check before anything else is to see if both strings have the same length
    if(len(firstStr) != len(secondStr)): 
        return False 
    
    # Create two dictionaries that store the letters in each string and their number of occurences
    firstStrDict = {}
    secondStrDict = {}

    for letter in firstStr: 
        firstStrDict[letter] = firstStrDict.get(letter, 0) + 1
    
    for letter in secondStr: 
        secondStrDict[letter] = secondStrDict.get(letter, 0) + 1
    
    # Iterate through one of the dictionaries and check if the other dictionary contains the same
    # key and number of occurences per character
    for letter in firstStrDict: 
        if secondStrDict.get(letter) == None or secondStrDict.get(letter) != firstStrDict.get(letter): 
            return False
    return True 

print("Result:", validAnagram("a", "ab"))