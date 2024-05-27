def isPalindrome(someStr: str) -> bool: 
    """
    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all 
    non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters 
    and numbers.

    Given a string s, return true if it is a palindrome, or false otherwise.
    """
    # Create a string that only contains alphanumeric characters
    alphaNumericStr = "".join(ch.lower() for ch in someStr if ch.isalnum())
    
    # Check if the alphanumeric string has a length of one or 0
    if(len(alphaNumericStr) == 1 or len(alphaNumericStr) == 0): 
        return True
    
    # Create two pointers, one that starts at the beginning of the string and the other at the end of the string
    rightPtr = len(alphaNumericStr) - 1

    # Only need to increment both pointers up to the middle of the string
    for leftPtr in range(len(alphaNumericStr)//2): 
        if alphaNumericStr[leftPtr] == alphaNumericStr[rightPtr]: 
            rightPtr -= 1
            continue
        elif alphaNumericStr[leftPtr] != alphaNumericStr[rightPtr]:
            return False 
        elif leftPtr == rightPtr: 
            return True 
    return True 

print("Result:", isPalindrome("A man, a plan, a canal: Panama"))