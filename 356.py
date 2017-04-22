n, m = map(int, input().split())

A = []
for i in range(n):
    summa = sum(list(map(int, input().split())))
    A.append(summa)
max_summa = max(A)
index = A.index(max_summa)

print(summa, '\n', index)

