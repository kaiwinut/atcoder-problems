from itertools import accumulate


h,w = map(int,input().split())
x = [[0] + list(map(int, input().split())) for _ in range(h)]
x = [[0] * (w+1)] + x

acc = []

for i in range(len(x)):
    acc.append(list(accumulate(x[i])))

for i in range(1, len(acc)):
    for j in range(len(acc[0])):
        acc[i][j] += acc[i-1][j]

q = int(input())
for _ in range(q):
    a,b,c,d = map(int,input().split())
    print(acc[c][d] - acc[a-1][d] - acc[c][b-1] + acc[a-1][b-1])