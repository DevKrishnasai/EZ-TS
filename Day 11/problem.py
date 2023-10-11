n = int(input())
l = list(map(int,input()))
pre =0
for i in l:
    if i>pre:
        pre+=i

print(pre)
