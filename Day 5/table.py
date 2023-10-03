#table
def table(x,n):
    if n==11:
        return     
    print(x,'*',n,'=',x*n)
    table(x,n+1)
    
x=int(input())
table(x,1)