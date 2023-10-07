def fun(arr,i):
    if len(arr)==0:
        return i
    if arr[0]>i:
        i=arr[0]
    return fun(arr[1:],i)

print(fun([1,9,4,2],0))
