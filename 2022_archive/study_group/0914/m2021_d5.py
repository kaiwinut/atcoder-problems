from itertools import accumulate

N = int(input())
A = list(map(int, input().split()))
S = list(map(int, input().split()))
mod = 998244353

indexes = {}
prefix_sums = list(accumulate(S))
ans = 0
l = 0
for r in range(N):
    if A[r] in indexes:
        l = max(l, indexes[A[r]])
    indexes[A[r]] = r + 1
    ans += prefix_sums[r-l]
    ans %= mod
    print(l, r)

print(ans)