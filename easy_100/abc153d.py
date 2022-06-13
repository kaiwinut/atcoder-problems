H = int(input())

cnt = 0
while H > 0:
    H = H // 2
    cnt += 1

s = 0
for i in range(cnt):
    s += 2 ** i

print(s)