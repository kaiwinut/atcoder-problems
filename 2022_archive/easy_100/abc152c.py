N = int(input())
P = list(map(int, input().split()))

cnt = 0
local_min = N+1
for p in P:
    if p < local_min:
        local_min = p
        cnt += 1

print(cnt)