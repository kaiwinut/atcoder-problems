# しゃくとり

n,k = map(int,input().split())
a = [0] + list(map(int,input().split()))

r = [0] * (n + 1)

for i in range(1, n + 1):
    if i == 1:
        r[1] = 1
    else:
        r[i] = r[i-1]
    
    while r[i] < n and a[r[i]+1] - a[i] <= k:
        r[i] += 1

cnt = 0
for i in range(1, n):
    cnt += r[i] - i
print(cnt)

# Binary

# n,k = map(int,input().split())
# a = list(map(int,input().split()))

# def check(num, i):
#     if a[i] - num <= k:
#         return True
#     return False

# e = []
# for i in range(len(a) - 1):
#     l, r = 0, n - 1
#     while l < r:
#         m = (l + r) // 2
#         if m == l:
#             if check(a[i], l+1):
#                 l = m + 1
#             break
#         if check(a[i], m):
#             l = m
#         else:
#             r = m - 1
#     e.append(l)

# cnt = 0
# for i in range(len(a) - 1):
#     cnt += e[i] - i

# print(cnt)