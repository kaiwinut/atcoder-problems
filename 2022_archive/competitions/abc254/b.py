N = int(input())

a = [[0] * (i + 1) for i in range(N)]

for i in range(N):
    for j in range(i+1):
        if j == 0 or i == j:
            a[i][j] = 1
        else:
            a[i][j] = a[i-1][j-1] + a[i-1][j]

for i in range(N):
    print(' '.join([str(s) for s in a[i]]))