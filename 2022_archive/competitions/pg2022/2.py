n = int(input())
a = list(map(int,input().split()))

d = {a[i]: i for i in range(len(a))}

a.sort()

ind = []
for e in a[n:2*n]:
    ind.append(d[e])

ind.sort()

for idx in ind:
    print(idx+1)