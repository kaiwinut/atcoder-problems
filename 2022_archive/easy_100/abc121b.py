N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
for i in range(N):
    s = 0
    for j in range(M):
        s += A[i][j] * B[j]
    if s + C > 0:
        cnt += 1

print(cnt)