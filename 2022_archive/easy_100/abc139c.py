import sys
n = int(input())
H = list(map(int, input().split()))

cnt = 0
m = []
if n == 1:
    print(0)
    sys.exit()
else:
    for i in range(1, len(H)):
        if H[i-1] >= H[i]:
            cnt += 1
        else:
            m.append(cnt)
            cnt = 0
        if i == len(H)-1:
            m.append(cnt)

print(max(m))