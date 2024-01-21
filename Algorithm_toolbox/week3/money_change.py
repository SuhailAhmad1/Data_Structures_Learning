def change(money):
    total = 0
    for i in [10,5,1]:
        coins = money//i
        total += coins
        money = money%i

    return total


if __name__ == '__main__':
    m = int(input())
    print(change(m))
