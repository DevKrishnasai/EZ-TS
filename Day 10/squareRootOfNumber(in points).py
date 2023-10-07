
n = int(input())
def squareRoot(l,r):
    if l>r:
        return r
    mid = (l+r)//2
    sq = mid*mid
    if sq==n:
        return mid
    elif sq<n:
        return squareRoot(mid+1,r)
    else:
        return squareRoot(l,mid-1)

print(squareRoot(0,n//2 +1))
