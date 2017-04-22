n, m = map(int, input().split())
maximum = 0

for i in range(n):
    lst = list(map(int, input().split()))
    best = max(lst)
    summa = sum(lst)
    if maximum < best:
        maximum = best
        allmax = 0
    if maximum == best and allmax < summa:
        allmax = summa
        index = i

print(index)
