from collections import defaultdict
from collections import deque

n,m = map(int, input().split())

g = defaultdict(list)
g_inv = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g_inv[b].append(a)

dist = [n + 1] * (n + 1)
dist[n] = 0

q = deque()
q.append(n)
while q:
    v = q.popleft()
    for u in g_inv[v]:
        if dist[u] != n + 1:
            continue
        dist[u] = dist[v] + 1
        q.append(u)

if dist[1] == n + 1:
    print(-1)

else:
    v = 1
    shortest = [v]
    while v != n:
        for u in sorted(g[v]):
            if dist[u] + 1 == dist[v]:
                shortest.append(u)
                v = u
                break
    print(*shortest)


# from collections import deque

# n,m = map(int, input().split())

# g = {}
# for _ in range(m):
#     a, b = map(int, input().split())
#     if a != b:
#         if a not in g:
#             g[a] = [b]
#         else:
#             if b not in g[a]:
#                 g[a].append(b)

# dist = [n + 1] * (n + 1) 
# dist[1] = 0

# ol = deque()
# ol.append(1)

# path = {}

# while len(ol) > 0:
#     i = ol.popleft()
#     if i in g:
#         update = False
#         for r in g[i]:
#             if dist[r] > dist[i] + 1:
#                 dist[r] = dist[i] + 1
#                 path[r] = [i]
#                 update = True

#             elif dist[r] == dist[i] + 1:
#                 dist[r] = dist[i] + 1
#                 path[r].append(i)
#                 update = True

#         if update:
#             ol.extend(g[i])

# # print(path)

# if n not in path:
#     print(-1)

# else:
#     shortest = {}
#     for k, v in path.items():
#         for e in v:
#             if e not in shortest:
#                 shortest[e] = [k]
#             else:
#                 shortest[e].append(k)
    
#     cr = 1
#     p = [cr]
#     for _ in range(dist[n]):
#         new = min(shortest[cr])
#         p.append(new)
#         cr = new

#     print(*p)