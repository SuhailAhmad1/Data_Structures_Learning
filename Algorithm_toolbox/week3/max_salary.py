from itertools import permutations

def find_max(nums):
    max = -1000000000
    max_index = -1
    for i in range(len(nums)):
        if int(nums[i]) > max:
            max = int(nums[i])
            max_index = i
    nums.pop(max_index)
    return max, nums

def largest_number_naive(numbers):
    res = ""
    n = len(numbers)
    nums = numbers
    for n in range(n):
        m_digit, nums = find_max(nums)
        
        res= res+str(m_digit) if int(res+str(m_digit)) > int(str(m_digit)+res) else str(m_digit)+res
    return res
        


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_naive(input_numbers))


