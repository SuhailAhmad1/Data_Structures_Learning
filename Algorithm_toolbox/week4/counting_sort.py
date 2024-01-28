def counting_sort(nums):
    count_dict = {}
    for i in range(10):
        count_dict[i] = 0
    for i in nums:
        count_dict[i] += 1

    res = []
    for k in count_dict:
        if count_dict[k] != 0:
            res.extend([k]*count_dict[k])
    return res

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(counting_sort(nums))