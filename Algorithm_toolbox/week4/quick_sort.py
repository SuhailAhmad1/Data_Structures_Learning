def partition_last_pivot(arr, l, r):
    pivot = arr[r]
    i = l
    j = r-1
    
    while i < j:
        while i < r and arr[i] <= pivot:
            i+=1
        while j > l and arr[j] > pivot:
            j-=1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        
    if arr[i] > pivot:
        arr[i], arr[r] = arr[r], arr[i]
        
    return i

def partition_first_pivot(arr, l, r):
    pivot = arr[l]
    i  = l+1
    j = r

    while i < j:
        while i < r and arr[i] <= pivot:
            i+=1
        while j > l and arr[j] > pivot:
            j-=1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        
    if arr[j] < pivot:
        arr[j], arr[l] = arr[l], arr[j]
    
    return j

def quick_sort(arr, l, r):
    if l < r:
        p = partition_first_pivot(arr, l, r)
        quick_sort(arr, l, p-1)
        quick_sort(arr, p+1, r)    



arr = [6, 4, 2, 3, 9, 8, 9, 4, 7, 6, 1]
quick_sort(arr, 0, len(arr)-1)
print("After partition : ", arr)