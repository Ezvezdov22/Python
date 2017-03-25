A = list(map(int, input().split()))
B=[]
for i in range(len(A)):
 if A[i] > 0:
   B.append(A[i])
print(min(B))
