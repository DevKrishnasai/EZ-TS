#All cases O(n^2)
#(n^2)/2 comparisons.
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        index = i
        print(arr,"out")

        for j in range(i + 1, n):
            if arr[j] < arr[index]:
                index = j
        arr[i], arr[index] = arr[index], arr[i]
        print(arr)

    return arr

my_list = list(map(int,input().split()))
sorted_list = selection_sort(my_list)
print(sorted_list)
