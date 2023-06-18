n,k = map(int, input().split())
h = [int(input()) for _ in range(n)]

h.sort()

min_d = 10 ** 10
for i in range(len(h) - k + 1):
    if h[i + k - 1] - h[i] < min_d:
        min_d = h[i + k - 1] - h[i]

print(min_d)