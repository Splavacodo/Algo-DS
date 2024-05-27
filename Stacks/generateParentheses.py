def generateParentheses(n: int) -> list[str]: 
    """
    Given n pairs of parentheses, write a function to generate all 
    combinations of well-formed parentheses.

    Approach:
    The simplest appraoch uses backtracking which uses two conditions that ensures a valid
    combination is made. A stack will be used to manage the open and closing parentheses.

    An opening parenthesis should be added to the stack if the number of opening parens is
    less than n. 

    A closing parenthesis can be added as long as the open paren count is greater than the closing
    paren count. 

    A combination is valid if the number of open parens matches the number of closing parens and
    if the number of closing parens matches n.
    """
    parenStack = []
    res = []

    def backtrack(openN, closedN): 
        if openN == closedN and closedN == n: 
            res.append("".join(parenStack))
            return 
        
        if openN < n: 
            parenStack.append("(")
            backtrack(openN + 1, closedN)
            parenStack.pop()
        
        if closedN < openN:  
            parenStack.append(")")
            backtrack(openN, closedN + 1)
            parenStack.pop()
    
    backtrack(0, 0)
    return res

print("Result:", generateParentheses(3))