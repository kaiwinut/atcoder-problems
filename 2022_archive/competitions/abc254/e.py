N, M = map(int, input().split())
links = [list(map(int, input().split())) for _ in range (M)]
Q = int(input())
queries = [list(map(int, input().split())) for _ in range (Q)]

graph = {i+1: [] for i in range(N)}
for l in links:
    a, b = l
    graph[a].append(b)
    graph[b].append(a)


## In this case we also need to expand the visited nodes
def dfs(v, k, s):
    if k <= 0:
        s.add(v)
        return s
    s.add(v)
    for child in graph[v]:
        s = s.union(dfs(child, k-1, s))
    return s


for q in queries:
    x, k = q
    print(sum(dfs(x, k, set())))