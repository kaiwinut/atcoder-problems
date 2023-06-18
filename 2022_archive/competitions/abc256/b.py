from collections import Counter
n = int(input())
A = list(map(int, input().split()))

p = 0
d = Counter()

for a in A:
    d[0] += 1
    for l in list(d.keys()):
        d[l+a] += d[l]
        del d[l]

for l in list(d.keys()):
    if l >= 4:
        p += d[l]

print(p)
