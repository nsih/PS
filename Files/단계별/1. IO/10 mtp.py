A = int(input())
B = int(input())

i = (B%10)
j = (B%100)//10
k = (B%1000)//100

print(A*i)
print(A*j)
print(A*k)
print(A*B)