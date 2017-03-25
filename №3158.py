A = list(map(int, input().split()))
b=max(A)
for i in range(len(A)):
 if A[i] == b:
  print(b,i)
  break
