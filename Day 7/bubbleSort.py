# Best - (n)
# worest and average - O(n^2)
# Best for small data and partially sorted data
def bubble_sort(arr):
    n = len(arr)
    swapped = True
    c=0
    while swapped:
        swapped = False
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                c+=1
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapped = True
    print(c)
    return arr


my_list = list(map(int,input().split()))
sorted_list = bubble_sort(my_list)
print(sorted_list)
