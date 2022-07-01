n = int(input())
sp = [input().split() for _ in range(n)]

d = {}
for i, (s,p) in enumerate(sp):
    d[(s,p)] = i+1

sp.sort(key=lambda x: (x[0], -int(x[1])))

for s,p in sp:
    print(d[(s,p)])