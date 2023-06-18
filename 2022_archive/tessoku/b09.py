n = int(input())
MAX = 1500

s = [[0] * (MAX + 2) for _ in range(MAX + 2)]

for _ in range(n):
    a,b,c,d = map(int, input().split())
    s[a+1][b+1] += 1
    s[c+1][d+1] += 1
    s[a+1][d+1] -= 1
    s[c+1][b+1] -= 1

z = [[0] * (MAX + 1) for _ in range(MAX + 1)]
for i in range(len(z)):
    for j in range(1, len(z[0])):
        z[i][j] = z[i][j-1] + s[i][j]

for i in range(1, len(z)):
    for j in range(len(z[0])):
        z[i][j] = z[i-1][j] + z[i][j]

cnt = 0
for i in range(len(z)):
    for j in range(len(z[0])):
        if z[i][j] > 0:
            cnt += 1
print(cnt)