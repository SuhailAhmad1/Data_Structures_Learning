def gcd(a,b):
    r = max(a,b)%min(a,b)
    if r == 0:
        return min(a,b)
    return gcd(r, min(a,b))
    
def lcm(a,b):
    return (a*b)//gcd(a,b)
if __name__ == '__main__':
    n, m = map(int, input().split())
    print(lcm(n,m))
