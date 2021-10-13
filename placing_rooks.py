MOD = 998244353

n, k = map(int, input().split())
x = n - k

num = 1
den = 1
s = 0
# print(x)
tden = 1
for i in range(x):
    v = pow(x-i, n, MOD) * num
    s = (s * den + ((-1)**i) * v * tden) % MOD
    #print(num, den, (x-i)**n, v, s )
    tden = (tden * den) % MOD
    num = (num * (x-i)) % MOD
    den = (den * (i+1)) % MOD

num = 1
den = 1
for i in range(x):
    num = (num * (n-i)) % MOD
    den = (den * (i+1)) % MOD
#print("=",  s, num, den)
s = ((1 + (k != 0)) * s * num * pow(den * tden, MOD-2, MOD) % MOD)
print(s)
