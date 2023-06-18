import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())

g = [[] for i in range(n+1)]
for _ in range(n-1):
    a, b = list(map(int, input().split()))
    g[a].append(b)
    g[b].append(a)

for i in range(len(g)):
    g[i].sort()

path = []

def dfs(cn, pn):
    path.append(cn)
    for nn in g[cn]:
        if nn != pn:
            dfs(nn, cn)
            path.append(cn)

dfs(1, None)

print(*path)