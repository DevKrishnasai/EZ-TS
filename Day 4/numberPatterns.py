#normal method
n = int(input())
for i in range(1,n+1):
    s=0
    for j in range(i+1,1,-1):
        s+=(10**(j-2))*i
    print(s)

#Using maths to get the pattern
b=1
for i in range(1,n+1):
    print(b*i)
    b = (b*10)+1

#Using maths to get the pattern
for i in range(1,n+1):
    print(((10**i)//9) * i)

