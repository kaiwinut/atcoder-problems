n = int(input())
t,a = map(int,input().split())
H = list(map(int,input().split()))

best = 10 ** 10
best_i = -1
for i, h in enumerate(H):
    tmp = t - h * 0.006
    if abs(tmp - a) < abs(t - best * 0.006 - a):
        best = h
        best_i = i+1
print(best_i)