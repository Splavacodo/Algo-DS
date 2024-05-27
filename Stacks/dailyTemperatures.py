def dailyTemperatures(temperatures: list[int]) -> list[int]: 
    """
    Given an array of integers temperatures represents the daily temperatures, return an 
    array answer such that answer[i] is the number of days you have to wait after the ith 
    day to get a warmer temperature. If there is no future day for which this is possible, 
    keep answer[i] == 0 instead.
    """
    result = [0 for _ in range(len(temperatures))]
    tempStack = []

    for idx, temp in enumerate(temperatures): 
        while tempStack and temperatures[tempStack[-1]] < temp: 
            prevTempIdx = tempStack.pop()
            result[prevTempIdx] = idx - prevTempIdx
        
        tempStack.append(idx)
    
    return result 

print("Result:", dailyTemperatures([73,74,75,71,69,72,76,73]))