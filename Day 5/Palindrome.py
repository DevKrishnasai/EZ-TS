n=input()

""" 
i,j=0,len(n)-1
while(i<j):
    if n[i]!=n[j]:
        print("False")
        break
    i+=1
    j-=1
else:
    print("True")

"""       
'''
for i in range(0,len(n)//2):
    if n[i]!=n[len(n)-i-1]:
        print("False")
        exit()
print("True")
'''
'''
print(n==n[::-1])
'''
l=len(n)
def palin(x,i=0):
    if i<l//2:
        if x[i]==x[l-i-1]:
            palin(x,i+1)
        else:
            return False
    return True


"""
def palin2(n,i=0,j=len(n)-1):
    if i<j:
        if n[i]==n[j]:
            palin2(n,i+1,j-1)
        else:
            return False
    return True


"""

print(palin(n))