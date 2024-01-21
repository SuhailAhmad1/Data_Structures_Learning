def pisano_period(m):
    n1, n2 = 0, 1
    for i in range(m * m):  
        n1, n2 = n2, (n1 + n2) % m
        if n1 == 0 and n2 == 1:
            return i + 1  


def fibonacci_huge(n,m):
    n = n % pisano_period(m)
    if n <= 1:
        return n
    prev = 0
    curr = 1
    for i in range(n-1):
        prev, curr = curr, (prev+curr)

    return curr % m

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge(n, m))
