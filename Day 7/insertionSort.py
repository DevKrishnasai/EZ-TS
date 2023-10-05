# n(n-1)/2 comparisons
# O(n^2)
# Best case - O(n)
def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

my_list = list(map(int,input().split()))
sorted_list = insertion_sort(my_list)
print(sorted_list)
