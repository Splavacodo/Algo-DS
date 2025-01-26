def sortLists(L): 
    if len(L) <= 1: 
        return L[0]

    mid = len(L) // 2
    leftHalf = L[:mid]
    rightHalf = L[mid:]

    leftSorted = sortLists(leftHalf)
    rightSorted = sortLists(rightHalf)
    
    return mergeLists(leftSorted, rightSorted)

def mergeLists(leftSorted, rightSorted):
    combined = []
    leftArrPtr = 0
    rightArrPtr = 0
    
    while leftArrPtr < len(leftSorted) and rightArrPtr < len(rightSorted):
        if leftSorted[leftArrPtr] < rightSorted[rightArrPtr]: 
            combined.append(leftSorted[leftArrPtr])
            leftArrPtr += 1
        else: 
            combined.append(rightSorted[rightArrPtr])
            rightArrPtr += 1
    
    combined.extend(leftSorted[leftArrPtr:])
    combined.extend(rightSorted[rightArrPtr:])
    
    return combined

# Example usage:
sorted_list = sortLists([[3, 12, 19, 25, 36],[34, 89], [13, 26, 87], [28], [2, 10, 21, 29, 55, 59, 61]])
print(sorted_list)
