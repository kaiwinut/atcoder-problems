import math

PRIME = 998244353

n,m,a,b = map(int,input().split())

if a <= n and b <= m:
    all_comb = math.factorial(n+m) // (math.factorial(n) * math.factorial(m))
    pre = math.factorial(a+b) // (math.factorial(a) * math.factorial(b))
    post = math.factorial(n+m-a-b) // (math.factorial(n-a) * math.factorial(m-b)) 
    print((all_comb - pre * post) % PRIME)

else:
    all_comb = math.factorial(n+m) // (math.factorial(n) * math.factorial(m))
    print(all_comb)