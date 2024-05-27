def countGroups(related):
    count = 0
    numRows = len(related)
    related = convertToArray(related)
    
    for row in range(numRows):
        if related[row][row] == 1:
            count +=1
            dfs(row, numRows, related)
    return count

def dfs(idx, length,matrix):
    if matrix[idx][idx] == 0:
        return 
    for i in range(length):
        if matrix[idx][i]==1:
            matrix[idx][i]=0
            dfs(i,length,matrix)
            
            
def convertToArray(s):
    result = []
    for char in s:
        result.append([int(c) for c in char])
    return result    

print("Result:", countGroups(["1100","1110","0110","0001"]))