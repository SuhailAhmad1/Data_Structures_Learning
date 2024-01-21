def partition(arr, l, r):
    pivot = arr[l]
    j = l+1
    for i in range(l+1, r):
        if arr[i] <= pivot:
            if i!=j:
                arr[i], arr[j] = arr[j], arr[i]
            j+=1
    arr[l], arr[j-1] = arr[j-1], arr[l]
    print(arr)
    return j-1

def quick_sort(arr):
    partition(arr, 0, len(arr))

arr = [6,4,2,3,9,8,9,4,7,6,1]
quick_sort(arr)
