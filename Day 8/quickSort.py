# Quick sort
# Average case and best case O(nlogn)
# Worest case O(n^2)
def partition(arr, low, high):
  pivot = arr[high]

  i = low - 1

  for j in range(low, high):
    if arr[j] <= pivot:
      i = i + 1
      (arr[i], arr[j]) = (arr[j], arr[i])
  (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])

  return i + 1

def quickSort(arr, low, high):
  if low < high:
    pivot = partition(arr, low, high)
    quickSort(arr, low, pivot - 1)
    quickSort(arr, pivot + 1, high)

array = list(map(int,input().split()))
print("The Original Array:", array)

size = len(array)
quickSort(array, 0, size - 1)
print('The Sorted Array:', array)

