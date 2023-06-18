h,w,n = map(int,input().split())
s = [[0] * (w + 2) for _ in range(h + 2)]
for _ in range(n):
    a,b,c,d = map(int,input().split())
    s[a][b] += 1
    s[a][d+1] -= 1
    s[c+1][b] -= 1
    s[c+1][d+1] += 1

z = [[0] * (w + 2) for _ in range(h + 2)]
for i in range(len(z)):
    for j in range(1, len(z[0])):
        z[i][j] = z[i][j-1] + s[i][j]

for i in range(1, len(z)):
    for j in range(len(z[0])):
        z[i][j] = z[i-1][j] + z[i][j]

for l in z[1:len(z)-1]:
    print(*l[1:len(l)-1])