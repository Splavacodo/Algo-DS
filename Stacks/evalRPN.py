def evalRPN(tokens: list[str]) -> int: 
    """
    You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

    Evaluate the expression. Return an integer that represents the value of the expression.

    Note that:

    - The valid operators are '+', '-', '*', and '/'.
    - Each operand may be an integer or another expression.
    - The division between two integers always truncates toward zero.
    - There will not be any division by zero.
    - The input represents a valid arithmetic expression in a reverse polish notation.
    - The answer and all the intermediate calculations can be represented in a 32-bit integer.
    """
    # Create a single stack that will hold all the numbers in the tokens
    # The stack will be popped twice when an operator is hit
    numStack = []

    for token in tokens: 
        if token not in "+-*/": 
            numStack.append(int(token))
        else: 
            num = numStack.pop()

            # Accessing the last element in the stack and updating it ensures the correct
            # order for subtraction and division
            if token == '+': 
                numStack[-1] += num
            elif token == '-': 
                numStack[-1] -= num 
            elif token == '*': 
                numStack[-1] *= num
            else:
                numStack[-1] = int(numStack[-1] / num)
    
    return numStack.pop()
    
print("Result:", evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))