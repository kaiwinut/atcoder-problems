a = int(input())
b = int(input())
c = int(input())
x = int(input())

cnt = 0
for i in range(a+1):
    for j in range(b+1):
        left = x - 500 * i - 100 * j
        if left % 50 == 0 and 0 <= left // 50 <= c:
            cnt += 1

print(cnt)