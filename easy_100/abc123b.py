T = [int(input()) for _ in range(5)]

max_diff = 0
for i in range(len(T)):
    if T[i] % 10 != 0:
        t = (T[i] // 10 + 1) * 10
        if t - T[i] > max_diff:
            max_diff = t - T[i]
        T[i] = t

print(sum(T) - max_diff)