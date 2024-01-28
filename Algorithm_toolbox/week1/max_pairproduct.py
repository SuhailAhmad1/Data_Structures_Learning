def max_pairwise_product(nums):
    max1 = -1
    max2 = -1
    for i in range(len(nums)):
        if nums[i] > nums[max1] or max1 == -1:
            max1 = i
    for i in range(len(nums)):
        if  i != max1 and (nums[i] > nums[max2] or max2 == -1):
            max2 = i
    return (nums[max1])*(nums[max2])


if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))

