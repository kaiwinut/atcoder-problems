from dis import dis


N = int(input())
K = int(input())
X = list(map(int, input().split()))

dist = 0
for i in range(N):
    dist += min(X[i], K-X[i])

print(dist*2)