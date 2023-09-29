#Missing element in list
n = list(map(int, input().split()))
total = 0
for i in range(0,len(n)+1):
    total^=i

print(total)
subtotal = 0
for i in range(0,len(n)):
    subtotal^=n[i]

print(total^subtotal)  #missing number is this
