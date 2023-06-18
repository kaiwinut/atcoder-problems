from bisect import bisect_left


n,k = map(int, input().split())
a = list(map(int, input().split()))

p = []
for i in range(1 << (n//2)):
    s = 0
    for j in range(n//2):
        if (i // (1 << j)) % 2 == 1:
            s += a[j]
    p.append(s)

q = []
for i in range(1 << (n - n//2)):
    s = 0
    for j in range(n - n//2):
        if (i // (1 << j)) % 2 == 1:
            s += a[n//2 + j]
    q.append(s)

q.sort()

for e in p:
    idx = bisect_left(q, k-e)
    if idx < len(q) and k-e == q[idx]:
        print('Yes')
        exit()

print('No')