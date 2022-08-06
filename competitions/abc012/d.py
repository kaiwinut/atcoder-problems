## Floyd–Warshall Algorithm

n,m = map(int, input().split())
abt = [list(map(int, input().split())) for _ in range(m)]

graph = [[float('inf')]*n for _ in range(n)]
for (a,b,t) in abt:
    graph[a-1][b-1] = t
    graph[b-1][a-1] = t

# Get all shortest path of each pair of verticies
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                graph[i][j] = 0
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
mxd = []
for g in graph:
    mxd.append(max(g))

print(min(mxd))


## TLE

# from heapq import heappop, heappush

# n,m = map(int, input().split())
# abt = [list(map(int, input().split())) for _ in range(m)]

# graph = [[] for _ in range(n)]
# for (a,b,t) in abt:
#     graph[a-1].append([t, b-1])
#     graph[b-1].append([t, a-1])

# def dijkstra(s):
#     d = [float('inf')]*n
#     d[s] = 0
#     visited = set({s})
#     que = []
#     for e in graph[s]:
#         heappush(que, e)
#     while que:
#         u, v = heappop(que)
#         if v in visited:
#             continue
#         d[v] = u
#         visited.add(v)
#         for e in graph[v]:
#             if e[1] not in visited:
#                 heappush(que, [e[0] + d[v], e[1]])
#     return d

# max_dist = []
# for i in range(n):
#     d = dijkstra(i)
#     max_dist.append(max(d))
# print(min(max_dist))