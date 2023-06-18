N = int(input())
a = list(map(int, input().split()))

cnt = 0
for i in range(len(a)):
    if i == a[a[i] - 1] - 1:
        cnt += 1

print(cnt // 2)