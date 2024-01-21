def fib(n):
    if n<=1:
        return n
    first = 0
    second = 1

    for _ in range(1, n):
        first, second = second, first+second
 
    return second

def find_last_digit(n):
    return fib(n%60) % 10

def last_digit(n):
    if n <=1:
        return n
    return (find_last_digit(n+2) - 1) % 10

if __name__ == '__main__':
    n = int(input())
    print(last_digit(n))