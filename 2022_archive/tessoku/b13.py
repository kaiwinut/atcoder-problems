from itertools import accumulate

n, k = map(int, input().split())
a = list(map(int, input().split()))
s = [0] + list(accumulate(a))
p = 1
cnt = 0
for i in range(1, n+1):
    while p < n + 1 and s[p] - s[i-1] <= k:
        p += 1
    cnt += p - i
print(cnt)

# from itertools import accumulate

# n,k = map(int,input().split())
# a = [0] + list(map(int,input().split()))

# acc = list(accumulate(a))

# r = [1] * (n+1)
# for i in range(1, n+1):
#     r[i] = r[i-1]
#     while r[i] < n + 1 and acc[r[i]] - acc[i-1] <= k:
#         r[i] += 1

# cnt = 0
# for i in range(1, n+1):
#     cnt += r[i] - i
# print(cnt)