N, A, B = map(int, input().split())

s = 0
for i in range(1, N+1):
    x_4 = i // 10000
    x_3 = (i - x_4 * 10000) // 1000
    x_2 = (i - x_4 * 10000 - x_3 * 1000) // 100
    x_1 = (i - x_4 * 10000 - x_3 * 1000 - x_2 * 100) // 10
    x_0 = i % 10
    if A <= x_0 + x_1 + x_2 + x_3 + x_4 <= B:
        s += i

print(s)