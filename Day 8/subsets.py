def is_subset_sum(arr, n, target_sum):
    if target_sum == 0:
        return True
    if n == 0:
        return False
    if arr[n - 1] > target_sum:
        return is_subset_sum(arr, n - 1, target_sum)
    return is_subset_sum(arr, n - 1, target_sum) or is_subset_sum(arr, n - 1, target_sum - arr[n - 1])

arr=list(map(int,input().split(", ")))
target_sum=int(input())
n=len(arr)
print(is_subset_sum(arr,n,target_sum))
