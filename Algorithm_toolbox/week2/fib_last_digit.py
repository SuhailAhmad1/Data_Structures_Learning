def first_60():
    previous = 0
    current  = 1
    first_60_last_digit = [previous, current]
    for _ in range(120-2):
        previous, current = current, previous + current
        first_60_last_digit.append(current % 10) 
    return first_60_last_digit

def fibonacci_last_digit(n):
    return first_60()[n%60]

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit(n))
