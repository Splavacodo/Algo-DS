class MinStack: 
    """
    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.

    You must implement a solution with O(1) time complexity for each function.
    """

    def __init__(self):
        self.__stack = []
        self.__minStack = []

    def push(self, val: int) -> None:
        self.__stack.append(val)
        if not self.__minStack: 
            self.__minStack.append(val)
        else: 
            minVal = min(val, self.__minStack[-1])
            self.__minStack.append(minVal)
        
    def pop(self) -> None:
        self.__stack.pop()
        self.__minStack.pop()
        
    def top(self) -> int:
        return self.__stack[-1]

    def getMin(self) -> int:
        return self.__minStack[-1]
