#floor of the the index if number not found
# import bisect
# l = list(map(int,input().split()))
# tar = int(input())
# res = bisect.bisect_left(l,tar)
# print(res)

# l = list(map(int,input().split()))
# tar = int(input())
# def binary(left,right,floor=-1):
#     if l[mid]==tar:
#         return mid
#     if left<=right:
#         mid = (left+right)//2
#         if l[mid]<tar:
#             floor = mid
#             return binary(mid+1,right)
#         if l[mid]>tar:
#             return binary(left,mid-1)
#     return floor

# floor= binary(0,len(l)-1)
# print(floor)

num = int(input())
first = 0
last = num//2
flag = 0
while first<=last:
    mid = (first+last)//2
    sq = mid*mid
    if sq==num:
        print(mid)
        flag=1
        break
    elif sq<num:
        floor = mid
        first = mid+1
    else:
        last = mid-1

