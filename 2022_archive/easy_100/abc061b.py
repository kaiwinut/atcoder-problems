from collections import Counter
n,m = map(int,input().split())
ab = [list(map(int,input().split())) for _ in range(m)]

d = Counter()
for (a,b) in ab:
    d[a] += 1
    d[b] += 1

for i in range(1,n+1):
    print(d[i])