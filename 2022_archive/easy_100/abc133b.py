from math import sqrt
n,d = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(i+1, n):
        dist_sq = 0

        for k in range(d):
            dist_sq += (X[i][k] - X[j][k]) ** 2
        
        if int(sqrt(dist_sq)) == sqrt(dist_sq):
            cnt += 1

print(cnt)