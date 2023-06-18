N = int(input())
A = list(map(int, input().split()))

## Fast

all = 1
bad = 1

for a in A:
    all *= 3
    if a % 2 == 0:
        bad *= 2

print(all - bad)

## Slow

# def get_nums(l):
#     ans = 0
#     if len(l) == 1:
#         return 2 if l[0] % 2 == 1 else 1
#     if l[0] % 2 == 1:
#         ans += 2 * (3 ** (len(l) - 1)) + get_nums(l[1:])
#     else:
#         ans += (3 ** (len(l) - 1)) + 2 * get_nums(l[1:])
#     return ans

# print(get_nums(A))