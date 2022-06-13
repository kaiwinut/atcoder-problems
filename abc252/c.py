n = int(input())
S = [input() for _ in range(n)]

cnt = [[0] * 10 for _ in range(10)]

for i in range(10):
    for num in range(10):
        for j in range(n):
            if int(S[j][i]) == num:
                cnt[num][i] += 1

mx = [0] * 10
for num in range(len(cnt)):
    for j in range(10):
        if mx[num] < j + 10 * (cnt[num][j] - 1):
            mx[num] = j + 10 * (cnt[num][j] - 1)

print(min(mx))