def find_index(k, arr, l, h):
    if l > h:
        return -1
    mid = (l+h)//2
    if k == arr[mid]:
        return mid
    if k > arr[mid]:
        l = mid+1
    else:
        h = mid-1
    return find_index(k, arr, l, h)
    
def find_all_index(key_arr, array):
    low, high = 0, len(array)-1
    res = []
    for k in key_arr:
        current_i = find_index(k, array, low, high)
        if current_i <= 0:
            res.append(current_i)
            continue
        index = current_i
        prev = index
        while index>=0:
            prev = index
            index = find_index(k, array, low, index-1)
            if index == -1:
                break
        res.append(prev)
    res = list(map(str, res))
    return " ".join(res)


if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split()))
    n2 = int(input())
    key_array = list(map(int, input().split()))
    print(find_all_index(key_array, array))