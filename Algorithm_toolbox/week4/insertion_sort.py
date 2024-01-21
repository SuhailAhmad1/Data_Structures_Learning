def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        print(key)
        while j>=0 and key <arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
        
    return nums

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(insertion_sort(nums))