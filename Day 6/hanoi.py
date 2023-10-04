#Tower of hanoi problem
#method 1
def hanoi(s):
    if s==1:
        return 1
    return 2*hanoi(s-1)+1
print(hanoi(2))

#MEthod 2
def hanoi(s):
    if s==1:
        return 1
    c1 = hanoi(s-1)
    c2 = hanoi(s-1)
    return c1+c2+1
print(hanoi(2))

#Method 3
n=3
print((2**n)-1)
