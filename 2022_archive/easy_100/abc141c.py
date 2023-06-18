N, K, Q = map(int, input().split())
A = [int(input()) for _ in range(Q)]

points = [K for _ in range(N)]

seen = {i: 0 for i in range(1, N+1)}
for a in A:
    seen[a] += 1

for k in seen.keys():
    points[k-1] += seen[k] - Q

for p in points:
    print('Yes' if p > 0 else 'No')