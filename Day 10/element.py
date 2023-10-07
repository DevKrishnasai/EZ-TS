l = list(map(int,input().split()))

def binary(left,right,tar,mid=0):
    if left>right:
        return l[mid]
    mid = (left+right)//2
    if l[mid]==tar:
        return l[mid]
    if l[mid]<tar:
        return binary(mid+1,right,tar)
    if l[mid]>tar:
        return binary(left,mid-1,tar)


print(binary(0,len(l)-1,4))
