def gcd(a,b):
    r = max(a,b)%min(a,b)
    if r == 0:
        return min(a,b)
    return gcd(r, min(a,b))
    
if __name__ == '__main__':
    n, m = map(int, input().split())
    print(gcd(n,m))
