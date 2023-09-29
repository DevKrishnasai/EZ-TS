#find number of 1 bits in the gievn number
x = int(input("Enter a number:"))

n=x
#using normal metho
c=0
while True:
    if n%2:
        c+=1
    if n==0:
        break
    n=n//2
print(c)


#Using and operator
n=x
c=0
while n:
    c+=1
    n=n&(n-1)

print(c)

#Using right hand side operator
n=x
c=0
while n:
    if n&1:
        c+=1
    n=n>>1
print(c)
