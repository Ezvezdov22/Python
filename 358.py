n, m = map(int, input().split())

#index=0
A=[]
maximum=0
allmax=0

tmp = []

for i in range(n):
    A.append(list(map(int, input().split())))
    best = max(A[i])
    if maximum <= best:
        maximum = best

for i in range(n):
    summa = sum(A[i])
    if max(A[i]) == maximum and allmax < summa:
            allmax = summa
            index = i

print(index)

