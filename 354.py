#import sys
n=int(input())
A=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i+j == n-1:
            A[i][j]=1
        elif i+j > n-1:
            A[i][j]=2
        print(A[i][j], end=" ")
    print()