A = list(map(int, input().split()))
B=[]
for i in range(len(A)):
 if A[i] % 2 == 1 :
   B.append(A[i])
if B==[]:
    print('0')
else:
    print(min(B))
