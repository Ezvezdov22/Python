# A = list(map(int, input().split()))
# p=int(input())
# for i in range(len(A)):
#     if A[i] < p:
#         print(i+1)
#         exit()
# print(len(A)+1)

#A = list(map(int, input().split()))
#p = int(input())


def line(A,p):
    i1 = 0
    i2 = len(A) - 1
    while i2 > i1:
        i = (i1 + i2) // 2
        if p > A[i]:
            i2 = i - 1
        else:
            i1 = i + 1

    return i1+1 if p>A[i1] else i1+2


A= [170,160,150,150,140]

assert(line(A,180)==2)




