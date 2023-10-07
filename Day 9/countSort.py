# Count sort
# O(n+k)  n is length of list and k is the max number of list
# ALl cases same O(n+k)
# iterate from left side of list then the count sort is stable
# In all other cases cont sort is not stablew
l = list(map(int,input().split()))
maxLen = max(l)+1
index = [0]*maxLen
for i in l:
    index[i] += 1

for i in range(1,len(index)):
    index[i]+=index[i-1]
print(index)

temp = [0]*len(l)
for i in l[::-1]:
    index[i] -= 1
    j = index[i]
    temp[j] = i

print(temp)
