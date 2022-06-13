N = int(input())

from math import sqrt

# O(root N)
is_sq = {i+1: False for i in range(N)}
for i in range(1, int(sqrt(N)) + 1):
    is_sq[i * i] = True

# Get all divisors of all nums \leq N
# O(N log N)
d = [[] for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(i, N+1, i):
        d[j].append(i)

# Count i / f(i) where f(i) is the largest square number among i's divisors
cnt = [0] * (N+1)
for i in range(1, N+1):
    f = 0
    for j in d[i]:
        if is_sq[j]:
            f = j
    cnt[i//f] += 1

# Since i / f(i) * j / f(j) will be a square number, considering all combinations,
#  the answer will be the square sum of cnt
ans = 0
for c in cnt:
    ans += c * c

print(ans)


## TLE

# from math import sqrt

# cnt = 0

# for n in range(1, N ** 2 + 1):
#     if int(sqrt(n)) == sqrt(n):
#         if n == 1:
#             cnt += 1
#         else:
#             for i in range(1, int(sqrt(n))):
#                 if n % i == 0 and n // i <= N:
#                     cnt += 2
#             cnt += 1

# print(cnt)