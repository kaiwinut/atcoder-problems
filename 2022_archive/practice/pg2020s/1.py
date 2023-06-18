n = int(input())

cnt = 0
for _ in range(n):
    s = input()
    if s == 'WA' or s == '-':
        cnt += 1

print(cnt * 5)