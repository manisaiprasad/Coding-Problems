# divisibility by strings
def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return (a // gcd(a, b)) * b


def findSmallestString(s, t):
    n, m = len(s), len(t)
    l = lcm(n, m)
    s1, t1 = "", ""
    for i in range(l//n):
        s1 += s
    for i in range(l//m):
        t1 += t
    if (s1 == t1):
        print(s1)
    else:
        print(-1)
