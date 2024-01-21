def fib(n):
    if n<=1:
        return n
    first = 0
    second = 1

    for _ in range(1, n):
        first, second = second, first+second
        
    return second


if __name__ == '__main__':
    n = int(input())
    print(fib(n))
