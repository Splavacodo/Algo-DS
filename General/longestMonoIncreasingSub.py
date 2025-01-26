def LMIS(A): 
    f = [1 for _ in range(len(A) + 1)]

    f[0] = 0

    for i in range(1, len(A) + 1): 
        for j in range(i): 
            if A[i - 1] > A[j] and f[i] < f[j + 1] + 1: 
                f[i] = f[j + 1] + 1
    
    return max(f)

A = [20, 5, 14, 8, 10, 3, 12, 7, 16]

print("Result:", LMIS(A))