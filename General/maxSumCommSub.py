def MSCS(A, B): 
    # Create an empty 2d array 
    f = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]

    for i in range(1, len(A) + 1): 
        for j in range(1, len(B) + 1): 
            if A[i - 1] == B[j - 1]: 
                if A[i - 1] > 0: 
                    f[i][j] = f[i - 1][j - 1] + A[i - 1]
                else: 
                    f[i][j] = f[i - 1][j - 1]
            else: 
                f[i][j] = max(f[i - 1][j], f[i][j - 1])

    return f[len(A)][len(B)]

A = [36, -12, 40, 2, -5, 7, 3]
B = [2, 7, 36, 5, 2, 4, 3, -5, 3]
# A = [-2, -5, -18, 1, -3, 70]
# B = [1, -10, -13, -12, -3, 70]

print("Result:", MSCS(A, B))