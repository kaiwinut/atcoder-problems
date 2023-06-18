n = int(input())
a = list(map(int, input().split()))

ans = 40
for ai in a:
    cnt = 0
    x = ai
    while x % 2 == 0:
        x >>= 1
        cnt += 1
    if cnt < ans:
        ans = cnt
print(ans)