# A = list(map(int, input().split()))
# def minimum(a):
#     b=min(a)
#     return(b)
# print(minimum(A))
 A=[1,2,3,4]
 def square(a):
     for i in range (len(a)):
         a[i]*= a[i]
     return a
  print(square(A))

