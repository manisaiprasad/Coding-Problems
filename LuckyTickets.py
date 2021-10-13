import os
from io import BytesIO
from math import trunc

input = BytesIO(os.read(0, os.fstat(0).st_size)).readline

MOD = 998244353
MODF = float(MOD)
SHRT = float(1 << 16)
ROOT = 3.0


def fmod(x): return x - MODF * trunc(x / MODF)


def mod_prod(a, b, c=0): return fmod(trunc(a / SHRT) *
                                     fmod(b * SHRT) + (a - SHRT * trunc(a / SHRT)) * b + c)


n, k = map(int, input().split())
n //= 2

inv = [1.0] * (9 * n + 2)
for i in range(2, 9 * n + 2):
    inv[i] = mod_prod(trunc(MODF / i), -inv[998244353 % i])

a = [int(i) for i in input().split()]
mi = min(a)

a = [ai - mi for ai in a]
a.remove(0)

b = [0.0] * 16
b[0] = 1.0

ans = 0.0
for i in range(9 * n + 1):
    ans = mod_prod(b[i & 15], b[i & 15], ans)

    s = 0.0
    for ai in a:
        s = mod_prod(b[(i - ai + 17) & 15], n * ai - (i - ai + 1), s)
    b[(i + 1) & 15] = mod_prod(s, inv[i + 1])

print(int(ans % MODF))
