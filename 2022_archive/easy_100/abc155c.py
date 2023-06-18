from collections import Counter
n = int(input())
s = [input() for _ in range(n)]

d = Counter()
for w in s:
    d[w] += 1

max_cnt = max(d.values())

for k in sorted(d.keys()):
    if d[k] == max_cnt:
        print(k)