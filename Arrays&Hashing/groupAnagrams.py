def groupAnagrams(strings: list[str]) -> list[str]: 
    """
    Given an array of strings strs, group the anagrams together. 
    You can return the answer in any order.

    Different Approaches: 
    Keep track of counts - 
    Takes advantage of the fact that there can only be 26 possible characters in a given string. An array of integers is created and 
    each index in the array represents a count for a character... a -> index 0 , b -> index 1. Each character's ascii value is 
    subtracted from the lowest one which is 'a'. Once an array has been filled in for a single string, it can then be case to a
    tuple and used as a key in a dictionary. 
        Time Complexity: O(n)
        Space Complexity: O(n)

    Hashmap - 
    Loop through each of the strings in the input list and sort each individual string. The sorted sting can be used
    as a key whose value will be a list of words that make up the same sorted string. The values of that map can then
    be looped through and added to a final list that's returned.
        Time Complexity: O(nlogn)
        Space Complexity: O(n)
    """
    # Create an empty dictionary that will have sorted words as its keys
    groupedAnagrams = {}
    
    
    # Loop through every string, and sort the current string
    # After the current string is sorted, use it as a key in the dictionary and add the original word to a list at that key
    for string in strings: 
        sortedStr = "".join(sorted(string))
        if sortedStr in groupedAnagrams: 
            groupedAnagrams[sortedStr].append(string)
        else: 
            groupedAnagrams[sortedStr] = [string]
    
    # After each anagram has been grouped, go through the values in the dictionary and add them to a resulting list
    anagramsList = []
    for group in groupedAnagrams.values(): 
        anagramsList.append(group)

    return anagramsList

print("Result:", groupAnagrams(["eat","tea","tan","ate","nat","bat"]))        