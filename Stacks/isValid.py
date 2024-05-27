def isValid(string: str) -> bool: 
    """
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
    """
    # Check if the length of the input string is even before checking if it's valid
    if len(string)%2 != 0:
        return False 

    # Create a stack that will store some of the characters in the input string
    # The only characters that will be added to the stack will be any opening brackets
    charStack = []

    # A hashmap would be useful for checking which bracket corresponds to a character without having
    # to check a bunch of conditions
    charMatches = { ")": "(", "}": "{", "]":"["}

    for char in string: 
        if char in charMatches:
            if charStack and charStack[-1] == charMatches[char]: 
                charStack.pop()
            else: 
                return False 
        else: 
            charStack.append(char)

    return charStack == [] 


print("Result:", isValid("()[]"))