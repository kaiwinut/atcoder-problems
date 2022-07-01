from bisect import bisect_right
from collections import Counter
n = int(input())
A = list(map(int, input().split()))

d = Counter(A)
cnt = 0
for i in range(1, 2 * 10 ** 5 + 1):
    for j in range(1, (2 * 10 ** 5 // i) + 1):
        cnt += d[i] * d[j] * d[i*j]

print(cnt)