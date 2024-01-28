def optimal_summands(n):
    if n<=2:
        return [n]
    summands = []
    sum = 0
    for i in range(1,n):
        if sum+i == n:
            summands.append(i)
            break
        if sum+i<n and sum+i+i<n:
            sum+=i
            summands.append(i)
    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
