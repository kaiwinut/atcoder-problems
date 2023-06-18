n,K = map(int, input().split())
A = list(map(int, input().split()))
berries = [list(map(int, input().split())) for _ in range(n)]

berries.sort(key=lambda x: (x[0] + x[1]))

lines = []
idx = 0
for j in reversed(range(len(A))):
    l = []
    for i, (x, y) in enumerate(berries[idx:]):
        if i > 0 and i % (j+1) == 0:
            l.append((x+1, y+1, x+2, y))
        if len(l) >= A[j]:
            lines += l
            idx = i+1
            break

k = min(len(lines), K)
print(k)
for i in range(k):
    print(*lines[i])