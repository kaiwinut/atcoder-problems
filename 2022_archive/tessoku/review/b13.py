from itertools import accumulate


n,k = map(int, input().split())
a = list(map(int, input().split()))

s = [0] + list(accumulate(a))

cnt = 0
r = 0

for i in range(1, n+1):
    while r < n + 1 and s[r] - s[i-1] <= k:
        r += 1

    cnt += r - i

print(cnt)