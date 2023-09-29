
import math
n = int(input())
print(math.log(n,2))   #It gives integer if its a perfect squareroot

c=0
k = 1          #for power of 2 k=1 for power 4 k=2 so on...
while n:
    c+=1
    n=n&(n-k)
if c==1:
    print("yes")
else:
    print("No")


