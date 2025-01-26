def knapsackExists(A, M): 
    f = [[0 for _ in range(M + 1)] for _ in range(len(A) + 1)]

    for i in range(len(f)):
        f[i][0] = 1

    for i in range(1, len(A) + 1): 
        for k in range(1, M + 1): 
            if k < A[i-1]: 
                f[i][k] = f[i - 1][k]
            else: 
                f[i][k] = max(f[i-1][k], f[i][k - A[i - 1]])
    
    return f[len(A)][M]

print("Result:", knapsackExists([3, 6, 2], 7))