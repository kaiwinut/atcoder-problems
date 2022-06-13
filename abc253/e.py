from itertools import accumulate

n,m,k = map(int,input().split())
mod = 998244353
# dp[i][j] is the number of posibilities when a_i equals j, given the a_1, ..., a_i
dp = [[0]*m for _ in range(n)]
dp[0] = [1]*m

for i in range(1,n):
    accum = list(accumulate(dp[i-1]))
    for j in range(m):
        if j-k>=0:
            dp[i][j] += accum[j-k] % mod
        if j+k<=m-1:
            dp[i][j] += (accum[m-1] - accum[j+k-1])%mod
        dp[i][j] %= mod
print(sum(dp[-1])%mod)