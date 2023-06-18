from re import L


N, M = map(int, input().split())
K = [list(map(int, input().split())) for _ in range(N)]

likes = {m+1: 0 for m in range(M)}
for k in K:
    for n in k[1:]:
        likes[n] += 1

cnt = 0
for m, l in likes.items():
    if l == N:
        cnt += 1

print(cnt)