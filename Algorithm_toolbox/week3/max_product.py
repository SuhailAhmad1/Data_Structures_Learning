from itertools import permutations


def max_dot_product(first_sequence, second_sequence):
    f_sorted = sorted(first_sequence)
    s_sorted = sorted(second_sequence)
    sum = 0
    for i in range(len(f_sorted)):
        sum += (f_sorted[i]*s_sorted[i])
    return sum


if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))
    
