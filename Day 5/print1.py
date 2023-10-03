# print 1 to n number using recursion
def print1(x):
    if x==0:
        return
    print1(x-1)
    print(x) 
n=int(input())
print1(n)
