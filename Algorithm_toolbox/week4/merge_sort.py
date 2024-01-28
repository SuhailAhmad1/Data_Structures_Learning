def merge(nums1, nums2):
    l1, l2 = len(nums1), len(nums2)
    res = []
    i = j = 0
    while i<(l1) and j<(l2):
        if nums1[i]<nums2[j]:
            res.append(nums1[i])
            i+=1
        else:
            res.append(nums2[j])
            j+=1
    res.extend(nums1[i:])
    res.extend(nums2[j:])
    return res


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums)//2
    return merge(merge_sort(nums[:mid]), merge_sort(nums[mid:]))

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(merge_sort(nums))