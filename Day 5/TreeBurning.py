#Tree is burning 
import random 
m=[[0]*4 for i in range(4)]
n=len(m)
for i in range(n):
    for j in range(n):
        m[i][j]=random.randint(0,1)
for i in range(n):
    for j in range(n):
        print(m[i][j],end=' ')
    print()
count=0
def fun(m,i,j,n):
    if m[i][j]==0:
        return
    if m[i][j]==1:
        m[i][j]=0   
    if i>0:
        fun(m,i-1,j,n)
    if i<n-1:
        fun(m,i+1,j,n)
    if j>0:
        fun(m,i,j-1,n)
    if j<n-1:
        fun(m,i,j+1,n)
i=int(input())
j=int(input())
fun(m,i,j,n)
for i in range(n):
    for j in range(n):
        if m[i][j]==1:
            count+=1
print(count)
