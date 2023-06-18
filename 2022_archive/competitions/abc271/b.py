n,q = map(int,input().split())
a = []
for _ in range(n):
    a.append(list(map(int,input().split()))[1:])

for _ in range(q):
    s,t = map(int,input().split())
    print(a[s-1][t-1])