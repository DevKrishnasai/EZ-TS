#Check sum using backtracking
def combinationSum(candidates, target):
    res=[]
    def backtrack(arr,n,target,arr2):
        if target==0:
            res.append(arr2)
            return
        for i in range(n,len(arr)):
            if arr[i]<=target:
                backtrack(arr,i,target-arr[i],arr2+[arr[i]])
    n=len(candidates)
    arr2=[]
    backtrack(candidates,0,target,arr2)
    return res

x = combinationSum([1,2,3,6,7],7)
print(x)
hasher = []
for i in x:
    if  hasher ==[] or  sorted(i) not in hasher:
        hasher.append(sorted(i))

for i in hasher:
    print(i)


