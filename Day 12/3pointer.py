l = list(map(int,input().split()))
j=0
i=0          # mid
k=len(l)-1
while i<=k:
    if l[i]==2:
        l[i],l[k]=l[k],l[i]
        k-=1
    elif l[i]==0:
        l[i],l[j]=l[j],l[i]
        j+=1
        i+=1
    else:
        i+=1
print(l)
print(i,j,k)
