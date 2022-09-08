import math

A = [1,2,3,4,5,6]
n = len(A)
for j in range(1,int(n/2)+1):
    k = n+1-j
    A[j] = A[j]+A[k]
    A[k] = A[j]-A[k]
    A[j] = A[j]-A[k]
    print(A)

