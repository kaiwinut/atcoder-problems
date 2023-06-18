from itertools import accumulate

n = int(input())
a = list(map(int, input().split()))

dist = [-1] * (n+1)

for i in range(len(a)):
    if dist[a[i]] == -1:
        dist[a[i]] = i
    else:
        dist[a[i]] = abs(i - dist[a[i]]) - 1

c = [0] * (2 * n - 1)

for d in dist[1:]:
    c[d] += 1

acc = list(accumulate(c))

for i in range(2 * n - 1):
    print(acc[i])