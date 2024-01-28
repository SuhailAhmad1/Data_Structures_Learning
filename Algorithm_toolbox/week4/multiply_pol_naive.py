def cal_multiple(n, p1, p2):
    res = [0]*(2*n-1)
    for i in range(len(p1)):
        for j in range(len(p2)):
            res[i+j] += (p1[i]*p2[j])
    return res

if __name__ == "__main__":
    n = int(input())
    p1 = list(map(int, input().split()))
    p2 = list(map(int, input().split()))
    print(cal_multiple(n, p1, p2))