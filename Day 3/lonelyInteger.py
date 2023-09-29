#loney
n = list(map(int,input().split()))
x=0
for i in range(len(n)):
    x^=n[i]
print(x)
