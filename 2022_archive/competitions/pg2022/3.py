n = int(input())
a = list(map(int,input().split()))

b = []
while a:
    v = a.pop()
    if v == 1:
        k = 2
        while b and b[-1] == k:
            b.pop()
            k += 1
    else:
        b.append(v)

print(sum(b))

# WA
# n = int(input())
# a = list(map(int,input().split()))

# s = sum(a)
# i = 0
# while i < len(a):
#     if a[i] == 1:
#         p = 0
#         while i+p+1 < len(a):
#             if a[i+p+1] - a[i] == p+1:
#                 p += 1
#             else:
#                 break
#         s -= (a[i] + a[i+p]) * (p + 1) // 2
#         i += p + 1

#     else:
#         i += 1

# print(s)