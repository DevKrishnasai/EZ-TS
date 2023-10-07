s = input()

# i = 0
# j = len(s)-1

# while i<=j:
#     if s[i]!=s[j]:
#         s=s[i+1:j]
#         i=-1
#         j=len(s)
#     i+=1
#     j-=1
# print(s)


def pal(i,j):
    while i>=0 and j<=len(s)-1 and s[i]==s[j]:
        i-=1
        j+=1
    if len(s[i+1:j])!=1:
        print(s[i+1:j])

for i in range(len(s)):
    pal(i,i)
